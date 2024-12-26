import requests
from bs4 import BeautifulSoup
import json
import logging

proxies = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#################################################################################################
# GeoNode                                                                                       #
#################################################################################################
# Geonode.com scraper
# Uses BeautifulSoup
class GeoNode:
    def scrape(this):
        proxy_site = ('https://proxylist.geonode.com/api/proxy-list?'
                      'limit=200'
                      '&page=1'
                      '&sort_by=lastChecked'
                      '&sort_type=desc'
                      '&protocols=http%2Chttps')
        logging.info("Starting to scrape from: " + proxy_site)
        r = requests.get(proxy_site)
        soup = BeautifulSoup(r.content, 'html.parser')
        site_json = json.loads(soup.text)
        for data in site_json['data']:
            if data.get('ip'):
                proxy = ':'.join([data.get('ip'), data.get('port')])
                proxies.append(proxy)
        logging.info("Finished scraping: " + proxy_site)
        return
