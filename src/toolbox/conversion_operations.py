import unicodedata
import xml.dom.minidom
from typing import List

from xsdata.formats.dataclass.serializers import XmlSerializer

from src.toolbox.flextext_models import Document, Item
from src.toolbox.uuid_generation import generate_uuid


def make_title(xml_it, title_lang, title_value):
    xml_title_item = Item()
    xml_title_item.type_value = "title"
    xml_title_item.lang = title_lang
    xml_title_item.value = title_value
    xml_it.item.append(xml_title_item)


def convert(toolbox_data, markers):
    # make document
    xml_doc = Document()
    xml_doc.version = "2"

    # interlinear_text
    xml_interlinear_text = xml_doc.InterlinearText()
    xml_interlinear_text.guid = generate_uuid(None)
    xml_doc.interlinear_text.append(xml_interlinear_text)

    # paragraphs and paragraph
    xml_paragraphs = xml_interlinear_text.Paragraphs()
    xml_paragraph = xml_paragraphs.Paragraph()
    xml_paragraph.guid = generate_uuid(None)
    xml_paragraphs.paragraph.append(xml_paragraph)
    xml_interlinear_text.paragraphs.append(xml_paragraphs)

    # phrases
    xml_phrases = xml_paragraph.Phrases()
    xml_paragraph.phrases = xml_phrases

    for phrase in toolbox_data:

        # test if valid marker
        is_valid = False
        for line in phrase:
            start_code = line[0]

            if markers.keys().__contains__(start_code):
                is_valid = True
                break
        if not is_valid:
            continue

        # make phrase
        xml_phrase = xml_phrases.Phrase()
        xml_phrase.guid = generate_uuid(None)
        xml_phrases.phrase.append(xml_phrase)

        # loop through each translation for a phrase
        for line in phrase:
            start_code = line[0]

            if not markers.keys().__contains__(start_code) or len(line) < 2:
                continue

            marker = markers[start_code]
            text_type = int(marker["text_type"])
            language = marker["\\lng"]
            text = line[1:]

            # title
            if start_code == "\\id":
                make_title(xml_interlinear_text, language, text)
                continue

            match text_type:
                # word
                case 1:
                    # item
                    phrase_item = Item()
                    phrase_item.type_value = "txt"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

                    # words
                    xml_words = xml_phrase.Words()
                    xml_phrase.words = xml_words

                    # each word
                    for word in text:
                        xml_word = xml_words.Word()
                        xml_word.guid = generate_uuid(None)

                        word_item = Item()
                        word_item.type_value = (
                            "txt"
                            if len(word) > 1 or unicodedata.category(word)[0] != "P"
                            else "punct"
                        )
                        word_item.lang = language
                        word_item.value = word
                        xml_word.item.append(word_item)
                        xml_words.word.append(xml_word)

                # morphemes
                case 2:
                    pass

                # lex. entries
                case 3:
                    pass

                # lex. gloss
                case 4:
                    pass

                # lex. gram info
                case 5:
                    pass

                # word gloss
                case 6:
                    # item
                    phrase_item = Item()
                    phrase_item.type_value = "gls"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

                    # words
                    xml_word_list: List[
                        "Document.InterlinearText.Paragraphs.Paragraph.Phrases.Phrase.Words.Word"
                    ] = []
                    if xml_phrase.words is not None:
                        xml_word_list = xml_phrase.words.word
                    for i in range(min(len(xml_word_list), len(text))):
                        xml_word = xml_word_list[i]
                        txt_item = xml_word.item[0]
                        gloss_word = text[i]
                        gloss_item = Item()
                        gloss_item.type_value = "gls"
                        gloss_item.lang = language
                        gloss_item.value = gloss_word
                        xml_word.item.append(gloss_item)

                        # morph item text
                        xml_morph_txt_item = Item()
                        xml_morph_txt_item.value = txt_item.value
                        xml_morph_txt_item.lang = txt_item.lang
                        xml_morph_txt_item.type_value = txt_item.type_value

                        # morph item gloss
                        xml_morph_gloss_item = Item()
                        xml_morph_gloss_item.value = gloss_item.value
                        xml_morph_gloss_item.lang = gloss_item.lang
                        xml_morph_gloss_item.type_value = gloss_item.type_value

                        # morphemes and morph
                        xml_morphemes = xml_word.Morphemes()
                        xml_morph = xml_morphemes.Morph()
                        xml_morph.item.append(xml_morph_txt_item)
                        xml_morph.item.append(xml_morph_gloss_item)
                        xml_morphemes.morph.append(xml_morph)
                        xml_word.morphemes.append(xml_morphemes)

                # word cat
                case 7:
                    pass

                # free translation
                case 8:
                    # item
                    phrase_item = Item()
                    phrase_item.type_value = "gls"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

                # literal translation
                case 9:
                    phrase_item = Item()
                    phrase_item.type_value = "lit"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

                # note
                case 10:
                    phrase_item = Item()
                    phrase_item.type_value = "note"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

    # convert to xml
    xml_serializer = XmlSerializer()
    converted_xml = xml_serializer.render(obj=xml_doc, ns_map={})

    temp = xml.dom.minidom.parseString(converted_xml)
    converted_xml = temp.toprettyxml()

    return converted_xml
