
from abc import ABCMeta
from amazon import Amazon
#from ebay import Ebay
from abc import ABCMeta, abstractmethod, abstractproperty

class Shop:
    __metaclass__ = ABCMeta

    def __init__(self, url):
        self.url = url

    @abstractproperty
    def price(self):
        """ Get price """
        pass

    @abstractproperty
    def number(self):
        """ Get shop number """
        pass

    @abstractproperty
    def currency(self):
        """ Get currency """
        pass

    @abstractproperty
    def photo(self):
        """ Get photo url """
        pass

    @abstractproperty
    def description(self):
        """ Get description """
        pass

Shop.register(Amazon)
#Shop.register(Ebay)
