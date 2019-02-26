from src.Requests.RequestHandler import RequestHandler
from src.DP.DictHandler import DictHandler
from bs4 import BeautifulSoup
import requests
import re


class OlxScrapper:

    @staticmethod
    def __get_page(product: str, page_number: int):

        request_url = str('https://www.olx.pl/oferty/q-' + product + '/').replace(' ', '-') if page_number == 1 else \
                      str('https://www.olx.pl/oferty/q-' + product + '/?page=' + str(page_number)).replace(' ', '-')
        data = {'q': product} if page_number == 1 else {'q': product, 'page': page_number}

        response = RequestHandler.request(request_url, 'GET', data=data)
        if type(response) != requests.models.Response or response.status_code != 200:
            return None

        return response

    @staticmethod
    def __get_additional_pages_number(first_page_source: str):
        soup = BeautifulSoup(first_page_source, 'html.parser')
        page_picker = soup.find('div', {'class': 'pager rel clr'})

        if page_picker:
            fieldset = page_picker.find('fieldset', {'class': 'fleft'})
            total_pages_raw = str(fieldset.find('input', {'type': 'submit', 'value': 'OK'})['class'])
            return int(re.search(r'\d+', total_pages_raw).group(0))

        return 0

    @staticmethod
    def __get_products_from_page(page_source: str):
        soup = BeautifulSoup(page_source, 'html.parser')
        products_table = soup.find('tbody')
        print(products_table)

    @staticmethod
    def __get_all_products(product: str, first_page: str, pages: int):
        pages = (first_page,) + tuple(OlxScrapper.__get_page(product, x) for x in range(2, pages + 1) if pages >= 2)
        return tuple(OlxScrapper.__get_products_from_page(page) for page in pages)

    @staticmethod
    def get_products(product: str):
        first_page = OlxScrapper.__get_page(product, 1)
        additional_pages = OlxScrapper.__get_additional_pages_number(first_page.text)
        products_list = OlxScrapper.__get_all_products(product, first_page.text, additional_pages)
