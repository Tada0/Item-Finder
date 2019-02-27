from src.Requests.RequestHandler import RequestHandler
from src.WebsitesScrappers.Scrapper import Scrapper
from src.DP.Product import Product
from bs4 import BeautifulSoup
import requests
import re


class OlxScrapper(Scrapper):

    @staticmethod
    def __get_page(product: str, page_nr: int):

        request_url = str('https://www.olx.pl/oferty/q-' + product + '/').replace(' ', '-') if page_nr == 1 else \
                      str('https://www.olx.pl/oferty/q-' + product + '/?page=' + str(page_nr)).replace(' ', '-')
        data = {'q': product} if page_nr == 1 else {'q': product, 'page': page_nr}

        response = RequestHandler.request(request_url, 'GET', data=data)
        if type(response) != requests.models.Response or response.status_code != 200:
            return None

        return response

    @staticmethod
    def __get_additional_pages_number(first_page: requests.models.Response):

        soup = BeautifulSoup(first_page.text, 'html.parser')
        page_picker = soup.find('div', {'class': 'pager rel clr'})

        if page_picker:
            fieldset = page_picker.find('fieldset', {'class': 'fleft'})
            total_pages_raw = str(fieldset.find('input', {'type': 'submit', 'value': 'OK'})['class'])
            return int(re.search(r'\d+', total_pages_raw).group(0))

        return 0

    @staticmethod
    def __get_item(raw_item: tuple):
        item_name = re.search(r'<strong>(.*?)</strong>', str(raw_item[0])).group(1)
        item_url = re.search(r'href="(.*?)">', str(raw_item[0])).group(1)
        item_price = int(re.search(r'\d+', str(raw_item[1])).group(0))
        return Product(item_name, item_url, item_price)

    @staticmethod
    def __get_products_from_page(page_source: requests.models.Response):

        soup = BeautifulSoup(page_source.text, 'html.parser')
        items_table = soup.find('tbody')
        items = items_table.find_all('tr', {'class': 'wrap'})
        items = [(i.find('h3', {'class': 'lheight22 margintop5'}), i.find('p', {'class': 'price'})) for i in items]
        return tuple(OlxScrapper.__get_item(item) for item in items)

    @staticmethod
    def __get_all_products(product: str, first_page: requests.models.Response, pages: int):

        pages = (first_page,) + tuple(OlxScrapper.__get_page(product, x) for x in range(2, pages + 1) if pages >= 2)
        return tuple(OlxScrapper.__get_products_from_page(page) for page in pages)

    @staticmethod
    def get_product_offers(product: str):

        first_page = OlxScrapper.__get_page(product, 1)
        additional_pages = OlxScrapper.__get_additional_pages_number(first_page)
        products_list_raw = OlxScrapper.__get_all_products(product, first_page, additional_pages)
        return tuple([item for page in products_list_raw for item in page])