import xml.etree.ElementTree as ET
import pandas as pd

class XML2DataFrame:

    def __init__(self, xml_path):
        xml_data  = ET.parse(xml_path).getroot()
        xml_data  = ET.tostring(xml_data)
        self.root = ET.XML(xml_data)

    def parse_root(self, root):
        return [self.parse_element(child) for child in iter(root)]

    def parse_element(self, element, parsed=None):
        if parsed is None:
            parsed = dict()
        for key in element.keys():
            parsed[key] = element.attrib.get(key)
        if element.text:
            parsed[element.tag] = element.text
        #for child in list(element):
        #    self.parse_element(child, parsed)
        return parsed

    def process_data(self,tag):
        structure_data = self.parse_root(self.root.findall(tag))
        return pd.DataFrame(structure_data)

#xml2df = XML2DataFrame(xml_data)
#xml_dataframe = xml2df.process_data()