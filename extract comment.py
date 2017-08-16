# parsing-XML
#extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
#comment counts from the XML data, compute the sum of the numbers in the file.
#To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML 
#for any tag named 'count' with the following line of code:counts = tree.findall('.//count')

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('counts:  ',len(counts))
sum = 0
for item in counts:
	sum = sum +int(item.text)
print(sum)


#print('sum:  ',sum)
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print('lat', lat, 'lng', lng)
    #print(location)
