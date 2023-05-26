from bs4 import BeautifulSoup
import requests

url = 'https://www.chrono24.com/iwc/pilots-watch-timezoner-top-gun-edition-iw395505-limited--id28255089.htm'

# understand headers arg better and specify what needed
headers = {"User-Agent":"Mozilla/5.0"}
html = requests.get(url, headers=headers)
page = BeautifulSoup(html.content, 'html.parser')

# searches for table that contains "Basic Info" text
basic_info_table = page.find_all(lambda tag: tag.name =='tbody' and "Basic Info" in tag.text)[0]
# gets rows of basic info table
table_rows = basic_info_table.find_all('tr')

# parses each row for td tags and puts pairings into lists
datalist = []
for row in table_rows:
    elements = row.find_all('td')
    test = tuple([element.text.strip() for element in elements])
    datalist.append(test)


# todo:
# work on element pairing, try to use dicts or touples
# get rid of basic info sublist since we know its the basic info table
# work on general mapping of key item pairings
# consistent structure to get ready for multiple pages
# MAKE MORE COMMITS WHILE WORKING, TOO MUCH CHANGING PER COMMIT