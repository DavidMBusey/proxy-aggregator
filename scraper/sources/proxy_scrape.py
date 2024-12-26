import requests
from bs4 import BeautifulSoup
import logging

proxies = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#################################################################################################
# ProxyScrape                                                                                   #
#################################################################################################
# Proxyscrape.com scraper
# Uses BeautifulSoup
def scrape(self):
    r = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
    soup = BeautifulSoup(r.content, 'html.parser')
    proxylist = soup.text.split()
    for proxy in proxylist:
        proxies.append(proxy)
    return