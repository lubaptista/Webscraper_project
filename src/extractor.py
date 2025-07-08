from config.settings import SETTINGS
from bs4 import BeautifulSoup

def extract_product_data(html):
    """
    Extrai dados dos produtos na página HTML.
    """
    soup = BeautifulSoup(html, "lxml")
    products = []

    product_boxes = soup.select(".thumbnail")
    
    for box in product_boxes:
        title_tag = box.select_one("a.title")
        title = title_tag.text.strip() if title_tag else "N/A"
        url = (
            "https://webscraper.io" + title_tag["href"]
            if title_tag and title_tag.has_attr("href")
            else "N/A"
        )

        price_tag = box.select_one("h4.price")
        price = price_tag.text.strip() if price_tag else "N/A"

        desc_tag = box.select_one("p.description")
        description = desc_tag.text.strip() if desc_tag else "N/A"

        product = {
            "title": title,
            "url": url,
            "price": price,
            "description": description,
        }
        products.append(product)

    return products
