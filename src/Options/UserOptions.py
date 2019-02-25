from src.DP.Singleton import Singleton


class UserOptions(metaclass=Singleton):
    def __init__(self):
        self.__products_list = ['Philips 240v']
