#amazon api wont work bcz it needs a phone number 

from sites_scrapers.get_data import get_data
from bs4 import BeautifulSoup as bs

site_url = 'https://amazon.com/s?k=' 

def amazon(searcharg):
    try:
        search_argument = searcharg.replace(" ","+")
        response = get_data(site_url, search_argument)
        soup = bs(response.content, 'html.parser')
        products = soup.select('[data-component-type="s-search-result"]')
        
        items = []
        for product in products:
            if len(items) >= 5: # This means we only need 5 items so the loop goes untile it fills the items list with 5 items
                break
            
            title = product.find('span', class_='a-size-medium a-color-base a-text-normal')
            price = product.find('span', class_='a-offscreen')
            
            if title and price:
                items.append({'title':title.get_text(),'price':price.get_text()})
            else:
                pass
    except:
        return []

    return items