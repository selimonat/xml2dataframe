import xml.etree.ElementTree as ET
import pandas as pd

class XML2DataFrame:
    #Class for converting xml files to Pandas DataFrame.
    #
    #Usage:
    #xml2df = XML2DataFrame(xml_path)
    #xml_dataframe = xml2df.process_data(filter), where filter is a string for 
    #a specific tag name. 
    
    def __init__(self, xml_path):
        #Creates an instance
        #xml_path: path to the xml file
        xml_data  = ET.parse(xml_path).getroot()
        xml_data  = ET.tostring(xml_data)
        self.root = ET.XML(xml_data)

    def process_data(self,tag="*"):
        #Filters xml elements with tag TAG and parses it into a DataFrame.
        #By default no filtering is applied
        structure_data = self.parse_root(self.root.findall(tag))
        #structure_data  is a list of dict
        return pd.DataFrame(structure_data)
    
    def parse_root(self, root):
        #Parses single elements
        return [self.parse_element(child) for child in iter(root)]

    def parse_element(self, element, parsed=None):
        #For each element create a dictionary
        if parsed is None:#initialize if not already
            parsed = dict()
            
        for key in element.keys():
            #Find attributes of the current element and create a dict
            parsed[key] = element.attrib.get(key)
            
        if element.text:#also add the tag content if present
            parsed[element.tag] = element.text
        #process children recursively. However, this is not straigtforward. 
        #This is because if children have same attributes, they will overwrite
        #the values that were assigned during previous calls. One remedy would 
        #be to modify key names by joining them with the tag name.
        #for child in list(element):
        #    self.parse_element(child, parsed)
        return parsed
