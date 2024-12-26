class ProxyFilter:
    def __init__(self, proxies):
        """
        Initialize the ProxyFilter with a list of proxies.
        Each proxy should be a dictionary with metadata such as type, speed, and anonymity.
        """
        self.proxies = proxies

    def apply_filters(self, filter_criteria):
        """
        Apply filters based on user-defined criteria.

        :param filter_criteria: A string of filters, e.g., "type=HTTP,speed<100,anonymity=high"
        :return: A filtered list of proxies
        """
        filters = self.parse_filter_criteria(filter_criteria)
        print(f"Parsed Filters: {filters}")  # Debugging

        filtered_proxies = self.proxies
        for key, condition in filters.items():
            filtered_proxies = [
                proxy for proxy in filtered_proxies if self.match_condition(proxy, key, condition)
            ]
            print(f"After filtering by {key}{condition}: {filtered_proxies}")  # Debugging

        return filtered_proxies

    def parse_filter_criteria(self, filter_criteria):
        """
        Parse the filter criteria string into a dictionary.
        """
        criteria = {}
        for criterion in filter_criteria.split(','):
            if '<' in criterion:
                key, value = criterion.split('<')
                criteria[key] = f"<{value}"
            elif '>' in criterion:
                key, value = criterion.split('>')
                criteria[key] = f">{value}"
            elif '=' in criterion:
                key, value = criterion.split('=')
                criteria[key] = value
        return criteria

    def match_condition(self, proxy, key, condition):
        """
        Check if a proxy matches a given condition.
        """
        if key not in proxy:
            print(f"Key {key} not found in proxy {proxy}")  # Debugging
            return False

        value = proxy[key]
        try:
            # Convert numerical fields for comparison
            if isinstance(value, str) and value.isdigit():
                value = int(value)
            elif isinstance(value, str):
                value = value.lower()

            if condition.startswith('<'):
                return float(value) < float(condition[1:])
            elif condition.startswith('>'):
                return float(value) > float(condition[1:])
            elif condition.startswith('='):
                return str(value).lower() == condition[1:].lower()
        except ValueError as e:
            print(f"Error matching condition: {e}, Value: {value}, Condition: {condition}")  # Debugging
            return False

        return False


# Example Usage
if __name__ == "__main__":
    proxies = [
        {"ip": "192.168.1.1", "port": "8080", "type": "HTTP", "speed": 50, "anonymity": "high"},
        {"ip": "192.168.1.2", "port": "3128", "type": "HTTPS", "speed": 120, "anonymity": "low"}
    ]

    filter_criteria = "type=HTTP,speed<100,anonymity=high"
    proxy_filter = ProxyFilter(proxies)
    filtered = proxy_filter.apply_filters(filter_criteria)
    print(f"Filtered Proxies: {filtered}")
