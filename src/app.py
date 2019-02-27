from src.WebsitesScrappers.AllegroScrapper import AllegroScrapper
from src.WebsitesScrappers.OlxScrapper import OlxScrapper
from src.UrlHandling.FileHandler import FileHandler
from src.UrlHandling.MailHandler import MailHandler
from src.Options.UserOptions import UserOptions
import time

if __name__ == "__main__":

    def check_for_new_products():

        def get_products(p): return OlxScrapper.get_product_offers(p) + AllegroScrapper.get_product_offers(p)

        print('Looking for New Products...')
        all_products = [item for p in tuple(map(get_products, UserOptions().get_products_list())) for item in p]
        new_products = FileHandler.check_with_existing_products('Resources/aul.txt', all_products)
        print('Found Some New Products') if new_products else print('Nothing New Found')

        FileHandler.add_new_products('Resources/aul.txt', new_products)
        FileHandler.delete_old_products('Resources/aul.txt', 30)

        MailHandler.send_mail(new_products, UserOptions().get_user_mail())

    while True:
        check_for_new_products()
        print('Going To Sleep for an hour....\n')
        time.sleep(60 * 60)  # Do this shit every hour
