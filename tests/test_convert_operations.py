from xsdata.formats.dataclass.serializers import XmlSerializer

from src.toolbox.flextext_models import Document


def test_serializing():
    doc = Document()

    xml_serializer = XmlSerializer()
    xml = xml_serializer.render(obj=doc, ns_map={})

    print(xml)
    assert xml is not None
