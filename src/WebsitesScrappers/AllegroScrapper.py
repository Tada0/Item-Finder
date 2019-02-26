from src.Requests.RequestHandler import RequestHandler
from src.DP.DictHandler import DictHandler
from src.DP.Product import Product
from bs4 import BeautifulSoup
import requests
import re


class AllegroScrapper:

    @staticmethod
    def __get_page(product: str, page_nr: int):

        data = {
            'order': 'm',
            'p': str(page_nr),
            'bmatch': 'baseline-n-ele-1-5-0131',
            'string': product.replace(' ', '%20')}

        request_url = 'https://allegro.pl/listing?' + '&'.join(map('='.join, data.items()))

        response = RequestHandler.request(request_url, 'GET', data=data, allow_redirects=True)
        if type(response) != requests.models.Response or response.status_code != 200:
            return None

        return response

    @staticmethod
    def __get_additional_pages_number(first_page_source: str):

        soup = BeautifulSoup(first_page_source, 'html.parser')
        page_picker = soup.find('div', {'class': 'm-pagination__list'})
        total_pages_raw = str(page_picker.find('span', {'class': 'm-pagination__text'}))
        return int(re.search(r'\d+', total_pages_raw).group(0))

    @staticmethod
    def __get_item(raw_item: tuple):

        item_name = re.search(r'<strong>(.*?)</strong>', str(raw_item[0])).group(1)
        item_url = re.search(r'href="(.*?)">', str(raw_item[0])).group(1)
        item_price = int(re.search(r'\d+', str(raw_item[1])).group(0))
        return Product(item_name, item_url, item_price)

    @staticmethod
    def __get_products_from_page(page_source: str):

        soup = BeautifulSoup(page_source, 'html.parser')
        items_table = soup.find('tbody')
        items = items_table.find_all('tr', {'class': 'wrap'})
        items = [(i.find('h3', {'class': 'lheight22 margintop5'}), i.find('p', {'class': 'price'})) for i in items]
        return tuple(AllegroScrapper.__get_item(item) for item in items)

    @staticmethod
    def __get_all_products(product: str, first_page: str, pages: int):

        pages = (first_page,) + tuple(AllegroScrapper.__get_page(product, x) for x in range(2, pages + 1) if pages >= 2)
        return tuple(AllegroScrapper.__get_products_from_page(page) for page in pages)

    @staticmethod
    def get_product(product: str):

        first_page = AllegroScrapper.__get_page(product, 1)
        additional_pages = AllegroScrapper.__get_additional_pages_number(first_page.text)
        products_list_raw = AllegroScrapper.__get_all_products(product, first_page.text, additional_pages)
        # products = tuple([item for page in products_list_raw for item in page])
