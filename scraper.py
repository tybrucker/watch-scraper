from bs4 import BeautifulSoup
import requests

# understand headers arg better and specify what needed
headers = {"User-Agent":"Mozilla/5.0"}

chrono24 = 'https://www.chrono24.com'

single_watch_url = 'https://www.chrono24.com/rolex/rolex-rolex-gmt-master-ii-batman-oyster-bracelet-126710blnr-2023--id20505792.htm'
watch_list_url = 'https://www.chrono24.com/rolex/index.htm'

def parse_watch_page(url):
    # get page as bs4 html parser
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

def parse_watch_list(url):
    # get page as bs4 html parser
    html = requests.get(url, headers=headers)
    page = BeautifulSoup(html.content, 'html.parser')

    # finds all links to watches on the list
    watches = page.find_all('a', 'article-item block-item rcard')
    print(parse_watch_page(chrono24 + watches[0]['href']))

    # for watch in watches:
        # print(i['href'])

parse_watch_list(watch_list_url)





# todo:
# work on general mapping of key item pairings
# consistent structure to get ready for multiple pages
# MAKE MORE COMMITS WHILE WORKING, TOO MUCH CHANGING PER COMMIT