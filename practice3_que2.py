## You are given a valid JSON document, and you have to print its score. The score is calculated by the sum of the scores of each element. For any element, the score is equal to the number of attributes it has.


import xml.etree.ElementTree as ET


xml_tree = ET.parse('test.xml')
counter = 0
iterbale_tree = xml_tree.iter()
for ele in iterbale_tree:
    counter = counter + 1 
print("The Score of given xml file is : ", counter)
