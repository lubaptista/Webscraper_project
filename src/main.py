from src.scraper import scrape_all
from src.storage import save_to_json, save_to_csv

if __name__ == "__main__":
    print("Iniciando scraper do site webscraper.io/test-sites/e-commerce/allinone ...")

    data = scrape_all()

    save_to_json(data, "data/processed/products.json")
    save_to_csv(data, "data/processed/products.csv")

    print("Scraping concluído!")
