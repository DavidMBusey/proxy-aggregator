import json

class ExportJSON:
    def __init__(self, output_file="proxies.json"):
        """
        Initialize the ExportJSON class.
        :param output_file: Name of the JSON file to save proxies to.
        """
        self.output_file = output_file

    def export(self, proxies):
        """
        Export proxies to a JSON file.
        :param proxies: List of proxies with metadata to export.
        """
        if not proxies:
            print("No proxies to export.")
            return

        try:
            with open(self.output_file, mode='w', encoding='utf-8') as file:
                json.dump(proxies, file, indent=4)
            print(f"Proxies successfully exported to {self.output_file}")
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
