### READING XML USING ELEMENT TREE ###

#This module is loaded and used as follows:

import xml.etree.ElementTree as ET

tree = ET.parse('example_document.xml')     # reads the xml file into a variable 'tree'
root = tree.getroot()       # the getroot() method returns the base level of xml tags (i.e. the first indent)

# the 'roots' of the structure allow us to search through their 'child' tags as follows

for child in root:
    print child.tag     # the .tag call returns the tag names contained within the 'root' parent structure

#You can then use 'x path' expressions, together with the find() method, to dig out data nested in multiple levels of the XML structure.

#For example, after parsing the file above:

title = root.find('./fm/bibl/title')    # searches for a <title> tag nested in the 'current/fm/bibl' level - the ./ means 'start at the current position/nesting level' (in this case it's 'root')

title_text = ""
for p in title:             # this iterates over the 'children' of the <title> element
    title_text += p.text    # for each 'child' element, take the 'text' of that element (by calling .text) and concatenate it onto the created empty string

#Note: .tag and .text are the two most common/useful attributes (of the 'elements') when working with XML using Python.

#To find multiple elements, use .findall() instead of .find()

#e.g.
    
for a in root.findall('./fm/bibl/aug/au'):      # this x-path expression takes you down into the <au> tag level
    email = a.find('email')
    if email is not None:
        print email.text

#Handling Attributes:

#The .text call can fish out the text BETWEEN OPEN/CLOSING TAGS, however, to fish out 'attributes' (which are stored WITHIN a single tag) we can use the .attrib["var"] method.
#e.g.
element.attrib["var"]       # will return the value/text stored in the variable 'var' as an attribute in the tag 'element'

