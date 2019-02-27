from src.DP.Singleton import Singleton


class UserOptions(metaclass=Singleton):
    def __init__(self):
        self.__products_list = ['Philips 240v']
        self.__user_mail = 'tomekholda@gmail.com'

    def get_products_list(self):
        return self.__products_list

    def get_user_mail(self):
        return self.__user_mail
