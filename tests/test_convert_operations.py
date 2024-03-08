from xsdata.formats.dataclass.serializers import XmlSerializer

from src.toolbox.flextext_models.flextext import Document, Item
from toolbox.uuid_generation import generate_uuid


def test_serializing():
    doc = Document()
    doc.version = 2

    # interlinear_text
    doc.interlinear_text = doc.InterlinearText()
    doc.interlinear_text.guid = generate_uuid(None)

    # item
    item1 = Item()
    item1.type_value = "title"
    item1.lang = "ext"
    item1.value = "ReallyUnglossed"
    doc.interlinear_text.item = item1

    # paragraph
    paragraphs = doc.interlinear_text.Paragraphs()
    paragraph = paragraphs.Paragraph()
    paragraph.guid = generate_uuid(None)
    paragraphs.paragraph.append(paragraph)
    doc.interlinear_text.paragraphs = paragraphs

    # phrase
    phrases = paragraph.Phrases()
    phrase = phrases.Phrase()
    phrase.guid = generate_uuid(None)
    paragraph.phrases = phrases
    phrases.phrase.append(phrase)

    # item
    item2 = Item()
    item2.type_value = "txt"
    item2.lang = "ext"
    item2.value = "Lorem ipsum"
    phrase.item.append(item2)

    # item
    item3 = Item()
    item3.type_value = "segnum"
    item3.lang = "en"
    item3.value = "1"
    phrase.item.append(item3)

    # words
    words = phrase.Words()
    word1 = words.Word()
    item11 = Item()
    item11.type_value = "txt"
    item11.lang = "ext"
    item11.value = "Lorem"
    word1.item = item11

    word2 = words.Word()
    item12 = Item()
    item12.type_value = "txt"
    item12.lang = "ext"
    item12.value = "ipsum"
    word2.item = item12

    word3 = words.Word()
    item13 = Item()
    item13.type_value = "punct"
    item13.lang = "ext"
    item13.value = "."
    word3.item = item13

    words.word.append(word1)
    words.word.append(word2)
    words.word.append(word3)
    phrase.words = words

    xml_serializer = XmlSerializer()
    xml = xml_serializer.render(obj=doc, ns_map={})

    print(xml)
    assert xml is not None
