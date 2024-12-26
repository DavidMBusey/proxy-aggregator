import argparse
from scraper.scraper import ProxyScraper
from validator.validate import ProxyValidator
from filters.filter import ProxyFilter
from exporters.export_csv import ExportCSV
from exporters.export_json import ExportJSON

def main():
    parser = argparse.ArgumentParser(description="ProxyScraper - A tool to scrape, validate, and export proxies.")
    parser.add_argument('--scrape', action='store_true', help="Scrape proxies from sources")
    parser.add_argument('--validate', action='store_true', help="Validate the scraped proxies")
    parser.add_argument('--export', choices=['csv', 'json'], help="Export validated proxies to a file")
    parser.add_argument('--filter', help="Apply filters (e.g., type=HTTP,speed<100)")
    args = parser.parse_args()

    if args.scrape:
        print("Scraping proxies...")
        scraper = ProxyScraper()
        scraper.scrape()

    if args.validate:
        print("Validating proxies...")
        validator = ProxyValidator()
        validator.validate()

    if args.filter:
        print(f"Filtering proxies with criteria: {args.filter}")
        proxy_filter = ProxyFilter()
        filtered_proxies = proxy_filter.apply_filters(args.filter)
        print(f"Filtered {len(filtered_proxies)} proxies")

    if args.export:
        print(f"Exporting proxies to {args.export} format...")
        if args.export == 'csv':
            exporter = ExportCSV()
            exporter.export()
        elif args.export == 'json':
            exporter = ExportJSON()
            exporter.export()

    print("Done!")

if __name__ == "__main__":
    main()
