from bs4 import BeautifulSoup
import requests

url = 'https://www.chrono24.com/iwc/pilots-watch-timezoner-top-gun-edition-iw395505-limited--id28255089.htm'

#understand headers arg better and specify what needed
headers = {"User-Agent":"Mozilla/5.0"}
html = requests.get(url, headers=headers)
page = BeautifulSoup(html.content, 'html.parser')

#possibly change to find better way of getting tables needed instead of all tables
info_tables = page.find_all('table')


#use bs4 navigation features
for table in info_tables:
    #bodys would be children to tables
    sections = table.find_all('tbody')
    for section in sections:
        #rows would be children to bodys
        rows = section.find_all('tr')
        for row in rows:
            #elements (td's) would be children to rows
            elements = row.find_all('td')
            for element in elements:
                print(element.text)