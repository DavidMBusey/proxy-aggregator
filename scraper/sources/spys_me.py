import requests
import logging
import re

proxies = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#################################################################################################
# SPYS ME                                                                                       #
#################################################################################################
# Spys.me scraper
# Type: HTTP/HTTPS/SOCKS(?) - possibly all
# Anonymity: ALL
class SpysMe:
    def scrape(self):
        proxy_site = 'https://spys.me/proxy.txt'
        proxy_site = 'https://spys.me/socks.txt'
        r = requests.get(proxy_site)
        spys_me_proxies = r.text
        pattern = re.compile('\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?')
        matcher = re.findall(pattern, spys_me_proxies)
    # with open(pathTextFile, "a") as txt_file:
    #     for proxy in matcher:
    #         txt_file.write(proxy + "\n")
