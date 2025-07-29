import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Website {url} is ONLINE.")
        else:
            print(f"Website {url} is OFFLINE or returned status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Website {url} is OFFLINE. Error: {e}")

if __name__ == "__main__":
    url = "https://www.google.com"
    check_website(url)
