from dotenv import load_dotenv
from os import environ
import requests

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#   This code is the code specialized to get the main response ,
#   and the site_scraping files will parse it based on the site and site's html .


#   The function should receive a url ending with the search query after the last slash (/) so the function works .

def get_data(site_url, search_argument):
  search_url = site_url + search_argument
  request_headers = {
    'User-Agent': USER_AGENT,
    'Viewport-Width':'347' #    This is to fool the site to think that we are using a real device and we are humans and not scraping bot
  }
  
  response = requests.get(search_url, headers=request_headers)
  return response