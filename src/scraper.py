from src.network import fetch_url
from src.parser import parse_html
from src.extractor import extract_product_data
from src.navigator import get_pagination_urls
from src.logger import setup_logger
from src.storage import save_to_json
from config.settings import SETTINGS
import time

logger = setup_logger("scraper", "data/logs/scraper.log")

def scrape_all():
    base_url = SETTINGS["BASE_URL"]
    
    # Carrega página inicial
    html = fetch_url(base_url)

    # Extrai URLs adicionais
    pages = [base_url]
    pages += get_pagination_urls(html, base_url)

    all_products = []

    for url in pages:
        print(f"Scraping: {url}")
        html = fetch_url(url)
        products = extract_product_data(html)
        all_products.extend(products)

    print(f"Produtor coletados:{all_products}")

    print(f"Coletados {len(all_products)} produtos.")

    return all_products
