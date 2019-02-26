from src.WebsitesScrappers.AllegroScrapper import AllegroScrapper
from src.WebsitesScrappers.OlxScrapper import OlxScrapper


if __name__ == "__main__":
    print(AllegroScrapper.get_product_offers("Philips 240v"))
    print(OlxScrapper.get_product_offers("Philips 240v"))
