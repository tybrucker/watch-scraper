from bs4 import BeautifulSoup
import requests

# understand headers arg better and specify what needed
headers = {"User-Agent":"Mozilla/5.0"}
chrono24 = 'https://www.chrono24.com'

single_watch_url = 'https://www.chrono24.com/rolex/rolex-rolex-gmt-master-ii-batman-oyster-bracelet-126710blnr-2023--id20505792.htm'
watch_list_url = 'https://www.chrono24.com/rolex/index.htm'

def parse_watch_page(url):
    """
    function to parse a single watch page
    :param url: url to a singular watch page
    :return: a list of descriptor/info tuples
    """

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
    """
    function to parse a watch list page
    :param url: url to a page to a list of watches and next butt
    :return: link to next?
    """

    # get page as bs4 html parser
    html = requests.get(url, headers=headers)
    page = BeautifulSoup(html.content, 'html.parser')

    # finds all links to watches on the list
    watches = page.find_all('a', 'article-item block-item rcard')
    # parses each watch page
    for watch in watches:
        print(parse_watch_page(chrono24 + watch['href']))

parse_watch_list(watch_list_url)

"""
todo
- try to speed the mf up, possibly slow due to bad internet
- finalize parse_watch_list:
    - store data from pages appropriately
    - get next link
"""