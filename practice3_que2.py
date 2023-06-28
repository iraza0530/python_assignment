import xml.etree.ElementTree as ET


xml_tree = ET.parse('test.xml')
counter = 0
iterbale_tree = xml_tree.iter()
for ele in iterbale_tree:
    counter = counter + 1 
print(counter)