from bs4 import BeautifulSoup
import requests

url = 'https://www.chrono24.com/rolex/rolex-rolex-gmt-master-ii-batman-oyster-bracelet-126710blnr-2023--id20505792.htm'

# understand headers arg better and specify what needed
headers = {"User-Agent":"Mozilla/5.0"}

def parse_watch_page(url):
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
    datalist.pop(0)
    return datalist



# todo:
# work on general mapping of key item pairings
# consistent structure to get ready for multiple pages
# MAKE MORE COMMITS WHILE WORKING, TOO MUCH CHANGING PER COMMIT