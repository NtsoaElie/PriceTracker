from bs4 import BeautifulSoup
import requests
import json

# Accept-Language: en-CA,en-US;q=0.9,en;q=0.8
# Accept: */*
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:158.0) Gecko/20100101 Firefox/158.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:158.0) Gecko/20100101 Firefox/158.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-CA,en-US;q=0.9,en;q=0.8"
}

# Pasted link from user
user_pasted_link = "https://www.apple.com/xf/shop/buy-iphone/iphone-18-pro"

# create new session
session = requests.Session()
session.headers.update(HEADERS)

def fetch_product_page(url: str) -> str | None:
    product_page = session.get(url, timeout=20)
    if product_page.status_code != 200:
        print(f"Failed to {url}: status: {product_page.status_code}")
        return None
    return product_page.text

if __name__ == "__main__":
    html = fetch_product_page(user_pasted_link)
    if html is not None:
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.find_all("script", type="application/ld+json"):
            if tag.string is None:
                continue
            data = json.loads(tag.string)
            print(json.dumps(data, indent=2, ensure_ascii=False))
            print("-----")




