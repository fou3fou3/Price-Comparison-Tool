#ebay needs a phone number also 

from sites_scrapers.get_data import get_data
from bs4 import BeautifulSoup as bs

site_url = 'https://ebay.com/sch/i.html?_nkw='

def ebay(searcharg):
    search_argument = searcharg.replace(" ","+")
    response = get_data(site_url, search_argument)
    soup = bs(response.content, 'html.parser')
    products = soup.find_all('div', class_='s-item__wrapper clearfix')
    del products[0]
    
    items = []
    for product in products:
        if len(items) >= 5:# This means we only need 5 items so the loop goes untile it fills the items list with 5 items
            break
        
        title = product.find('div', class_='s-item__title')
        price = product.find('span', class_='s-item__price')
        
        if title and price:
            items.append({'title':title.get_text(),'price':price.get_text()})
        else:
            pass
    
    return items
