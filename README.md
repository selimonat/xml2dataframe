# xml2dataframe
Reads xml data into a python DataFrame.

Converts an XML file to Pandas Data Frame.

## Example:

```python
xml_path      = "/Users/onat/export.xml";
from XML2DataFrame import XML2DataFrame;
x = XML2DataFrame(xml_path)
x.process_data()
```

If you are specifically interested to convert a given tag and ignore others, use it with an input argument as in
```python
x.process_data("Record")
```
This will only consider those elements.

## Possible Improvements:
Currently, when children's attributes in an xml file has the same attributes as parents, the values are overwritten. For this reason, children elements are not processed. This is recursively implemented in the current version, however commented out.
