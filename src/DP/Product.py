

class Product:
    def __init__(self, name: str, url: str, price: int):
        self.__name = name
        self.__url = url
        self.__price = price

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def get_price(self):
        return self.__price