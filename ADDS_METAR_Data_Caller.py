#!/usr/bin/env python3
import sys
import urllib3
import xml.etree.ElementTree as ET
http = urllib3.PoolManager()

file = open('identifiers.txt','a+')
file.seek(0,0)
identifiers = file.read()
file.close()

if len(identifiers) == 0:
    identifiers = input("Enter station IDs (seperate by commas, no spaces): ")
    
elif len(identifiers) != 0:
    print(identifiers)
    new_ident = input("Update station IDs (y or n): ")
    if new_ident == 'y':
        identifiers = input("Enter new station IDs (seperate  by commas, no spaces): ")
    else:
        new_ident == 'n'       

url = 'https://aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requesttype=retrieve&format=xml&hoursBeforeNow=1.25&fields=raw_text&mostRecentForEachStation=constraint&stationString={}'.format(identifiers)
r = http.request(
    'GET',
    url,
    timeout=4.0,
)

file = open("METAR.xml","w")
file.write(r.data.decode('utf-8'))
file.close()

tree = ET.parse('METAR.xml')
root = tree.getroot()

file = open("identifiers.txt","w")
file.write(identifiers)
file.close()

for raw_text in root.iter('raw_text'):
    print(raw_text.text)

input('Press ENTER to exit')