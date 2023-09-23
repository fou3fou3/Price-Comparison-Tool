from sites_scrapers.amazon import amazon
from sites_scrapers.ebay import ebay
from sites_scrapers.walmart import walmart

def scrap_sites(search_argument):
    data = {
        'search_arg': search_argument,
        'amazon': amazon(search_argument),
        'ebay': ebay(search_argument),
        'walmart': walmart(search_argument)
    }
    
    return data