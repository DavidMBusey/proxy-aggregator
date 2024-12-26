import socket
import time
import requests

class ProxyValidator:
    def __init__(self, test_url="https://httpbin.org/ip", timeout=5):
        """
        Initialize the ProxyValidator.
        :param test_url: URL to test proxy functionality.
        :param timeout: Timeout duration for proxy validation requests.
        """
        self.test_url = test_url
        self.timeout = timeout

    def validate_proxy(self, proxy):
        """
        Validate a single proxy.
        :param proxy: Proxy in the format {"ip": "IP", "port": "PORT", "type": "TYPE"}.
        :return: A dictionary with validation results (e.g., speed, anonymity).
        """
        start_time = time.time()
        proxy_address = f"{proxy['ip']}:{proxy['port']}"
        proxy_dict = {proxy['type'].lower(): proxy_address}

        try:
            response = requests.get(self.test_url, proxies=proxy_dict, timeout=self.timeout)
            response_time = round((time.time() - start_time) * 1000)  # Response time in ms

            if response.status_code == 200:
                # Check anonymity level
                reported_ip = response.json().get("origin")
                anonymity = "low" if proxy["ip"] in reported_ip else "high"

                # Add validation details to proxy
                proxy["speed"] = response_time
                proxy["anonymity"] = anonymity
                return proxy
        except requests.exceptions.RequestException:
            pass

        return None  # Return None if the proxy is invalid

    def validate_proxies(self, proxies):
        """
        Validate a list of proxies.
        :param proxies: List of proxies to validate.
        :return: List of valid proxies with validation details.
        """
        valid_proxies = []

        for proxy in proxies:
            print(f"Validating proxy: {proxy['ip']}:{proxy['port']} ({proxy['type']})")
            validated_proxy = self.validate_proxy(proxy)
            if validated_proxy:
                print(f"Proxy valid: {validated_proxy}")
                valid_proxies.append(validated_proxy)
            else:
                print(f"Proxy invalid: {proxy['ip']}:{proxy['port']}")

        return valid_proxies


# Example Usage
if __name__ == "__main__":
    proxies = [
        {"ip": "192.168.1.1", "port": "8080", "type": "HTTP"},
        {"ip": "192.168.1.2", "port": "3128", "type": "HTTPS"}
    ]

    validator = ProxyValidator()
    valid_proxies = validator.validate_proxies(proxies)

    print("Valid Proxies:")
    print(valid_proxies)
