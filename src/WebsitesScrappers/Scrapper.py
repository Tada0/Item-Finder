import requests


class Scrapper:

    @staticmethod
    def __get_page(product: str, page_nr: int):
        pass

    @staticmethod
    def __get_additional_pages_number(first_page: requests.models.Response):
        pass

    @staticmethod
    def __get_item(raw_item: tuple):
        pass

    @staticmethod
    def __get_products_from_page(page_source: requests.models.Response):
        pass

    @staticmethod
    def __get_all_products(product: str, first_page: requests.models.Response, pages: int):
        pass

    @staticmethod
    def get_product_offers(product: str):
        pass