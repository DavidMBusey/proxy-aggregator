import csv

class ExportCSV:
    def __init__(self, output_file="proxies.csv"):
        """
        Initialize the ExportCSV class.
        :param output_file: Name of the CSV file to save proxies to.
        """
        self.output_file = output_file

    def export(self, proxies):
        """
        Export proxies to a CSV file.
        :param proxies: List of proxies with metadata to export.
        """
        if not proxies:
            print("No proxies to export.")
            return

        # Extract headers from the first proxy
        headers = proxies[0].keys()

        try:
            with open(self.output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(proxies)
            print(f"Proxies successfully exported to {self.output_file}")
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
