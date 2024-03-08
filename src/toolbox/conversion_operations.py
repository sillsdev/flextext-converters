from xsdata.formats.dataclass.serializers import XmlSerializer

from src.toolbox.flextext_models.flextext import Document, Item
from toolbox.uuid_generation import generate_uuid


def convert(toolbox_data, markers):
    # make document
    xml_doc = Document()
    xml_doc.version = "2"

    # interlinear_text
    xml_interlinear_text = xml_doc.InterlinearText()
    xml_interlinear_text.guid = generate_uuid(None)
    xml_doc.interlinear_text.append(xml_interlinear_text)

    # assuming no title

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
        # make phrase
        xml_phrase = xml_phrases.Phrase()
        xml_phrase.guid = generate_uuid(None)
        xml_phrases.phrase.append(xml_phrase)

        for line in phrase:
            start_code = line[0]
            marker = markers[start_code]
            text_type = int(marker["text_type"])
            language = marker["lng"]

            match text_type:
                # word
                case 1:
                    # item
                    text = line[1:]
                    phrase_item = Item()
                    phrase_item.type_value = "txt"
                    phrase_item.lang = language
                    phrase_item.value = text
                    xml_phrase.item.append(phrase_item)

                    # words
                    xml_words = xml_phrase.Words()

                    # each word
                    for word in text:
                        xml_word = xml_words.Word()
                        xml_word.guid = generate_uuid(None)

                        word_item = Item()
                        word_item.type_value = "txt"
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
                    pass

                # word cat
                case 7:
                    pass

                # free translation
                case 8:
                    pass

                # literal translation
                case 9:
                    pass

                # note
                case 10:
                    pass

    xml_serializer = XmlSerializer()
    converted_xml = xml_serializer.render(obj=xml_doc, ns_map={})
    return converted_xml
