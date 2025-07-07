from src.network import fetch_url
from src.parser import parse_html
from src.extractor import extract_table_data
from src.navigator import get_next_page_url
from src.logger import setup_logger
from config.settings import SETTINGS
import time

logger = setup_logger("scraper", "data/logs/scraper.log")

def scrape_all():
    url = SETTINGS["BASE_URL"]
    all_data = []

    while url:
        logger.info(f"Scraping URL: {url}")
        html = fetch_url(url)
        if not html:
            logger.error(f"Falha ao buscar {url}")
            break

        soup = parse_html(html)
        page_data = extract_table_data(soup)
        all_data.extend(page_data)
        logger.info(f"Coletadas {len(page_data)} tabelas na página.")

        url = get_next_page_url(soup, SETTINGS["BASE_URL"])
        if url:
            time.sleep(SETTINGS["DOWNLOAD_DELAY"])

    return all_data
