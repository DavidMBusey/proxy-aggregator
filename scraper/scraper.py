from scraper.sources.proxyNova import ProxyNova
from scraper.sources.spys_me import SpysMe
from scraper.sources.spys_one import SpysOne
from scraper.sources.free_proxy_list import FreeProxyList
from scraper.sources.geonode import GeoNode

class ProxyScraper:
    def __init__(self):
        """
        Initialize the ProxyScraper.
        The scraper will collect proxies from multiple sources.
        """
        self.proxies = []

    def scrape_all_sources(self):
        """
        Scrape proxies from all integrated sources and aggregate them.
        :return: A list of proxies.
        """
        sources = [
            ("ProxyNova", ProxyNova),
            ("Spys.me", SpysMe),
            ("Spys.one", SpysOne),
            ("Free Proxy List", FreeProxyList),
            ("GeoNode", GeoNode),
        ]

        for name, source_class in sources:
            print(f"Scraping proxies from {name}...")
            self.proxies.extend(self.safe_scrape(source_class))

        print(f"Total proxies scraped: {len(self.proxies)}")
        return self.proxies

    @staticmethod
    def safe_scrape(source_class):
        """
        Safely execute a scraping class, catching errors to avoid crashes.
        :param source_class: The class responsible for scraping.
        :return: The result of the scrape or an empty list if an error occurs.
        """
        try:
            scraper_instance = source_class()
            return scraper_instance.scrape()
        except Exception as e:
            print(f"Error scraping with {source_class.__name__}: {e}")
            return []
