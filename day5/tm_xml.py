#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import xml.etree.ElementTree as ET
tree = ET.parse('date.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)

for node in root.iter('year'):
    print(node.tag,node.text)

#change xml
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update','yes')

tree.write('date.xml')

#delete xml content
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('output.xml')

#create xml
import xml.etree.ElementTree as ET
new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"age")
sex.text = '33'

name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age1 = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml)
et.write("test.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)
