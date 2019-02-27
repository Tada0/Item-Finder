from src.WebsitesScrappers.AllegroScrapper import AllegroScrapper
from src.WebsitesScrappers.OlxScrapper import OlxScrapper
from src.FileHandler.FileHandler import FileHandler


if __name__ == "__main__":
    all_products = OlxScrapper.get_product_offers("Philips 240v") + AllegroScrapper.get_product_offers("Philips 240v")

    new_products = FileHandler.check_with_existing_products('../Resources/aul.txt', all_products)
    FileHandler.add_new_products('../Resources/aul.txt', new_products)