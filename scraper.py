from bs4 import BeautifulSoup
import requests
import concurrent.futures

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
    print('entering parse_watch_page:' + url)
    
    html = requests.get(url, headers=headers)
    page = BeautifulSoup(html.content, 'lxml')
    
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

def parse_watch_list(url, brand_list):
    """
    function to parse a watch list page
    :param url: url to a page to a list of watches and next butt
    :return: link to next or None if none
    """
    print('entering parse_watch_list:' + url)

    html = requests.get(url, headers=headers)
    page = BeautifulSoup(html.content, 'lxml')

    # finds all links to watches on the list
    watches = page.find_all('a', 'article-item block-item rcard')
    
    # parses each watch page
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(parse_watch_page, chrono24 + watch["href"])
            for watch in watches
        ]
        
        for w in concurrent.futures.as_completed(futures):
            brand_list.append(w.result())
        
    #return link to next page, if no next return None
    try:
        next = page.find_all('a','paging-next')[0]
        print('returning:' + next['href'])
        return next['href']
    except:
        print('no next returning None')
        return None


def brand_handler(url):
    brand_watches = []
    link = url
    while(link != None):
        link = parse_watch_list(link, brand_watches)
    return brand_watches


print(brand_handler(watch_list_url))



def test_func(url):
    html = requests.get(url, headers=headers)
    page = BeautifulSoup(html.content, 'lxml')
    next = page.find_all('a','paging-next')
    print(next[0]['href'])


"""
todo
- fully implement brand_handler
- do more brands
- put in excel sheet
"""