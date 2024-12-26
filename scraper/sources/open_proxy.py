from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import logging

proxies = []
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#################################################################################################
# OpenProxy                                                                                     #
#################################################################################################
# OpenProxy.space scraper
# Type: HTTP/HTTPS/SOCKS(?) - possibly all
# Anonymity: ALL
class OpenProxy(object):
    def scrape(self):
        proxy_type = proxy_type.lower()
        if "http" in proxy_type or "https" in proxy_type or proxy_type == "any":
            proxy_site = 'https://openproxy.space/list/http'
            self.open_proxy_space_scrape_proxies(proxy_site)
        if "socks4" in proxy_type or proxy_type == "any":
            proxy_site = 'https://openproxy.space/list/socks4'
            self.open_proxy_space_scrape_proxies(proxy_site)
        if "socks5" in proxy_type or proxy_type == "any":
            proxy_site = 'https://openproxy.space/list/socks5'
            self.open_proxy_space_scrape_proxies(proxy_site)
        return

    # OpenProxy.space proxy scraper handler
    def open_proxy_space_scrape_proxies(proxy_site):
        logging.info("Starting to scrape from: " + proxy_site)
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        browser = webdriver.Edge(options=options)
        browser.get(proxy_site)
        proxies_data = browser.find_elements(By.CLASS_NAME, "data")[0].text
        for proxy in proxies_data.split():
            proxies.append(proxy)
