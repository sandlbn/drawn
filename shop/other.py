# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup


class Other:
    def __init__(self, url):
        self.item = url

    @property
    def title(self):
        """ return title of Item """
        soup = BeautifulSoup(
            urllib2.urlopen(self.item)
        )
        try:
            return soup.title.string
        except AttributeError:
            return None


    @property
    def price(self):
        """ return None """
        return None

    @property
    def currency(self):
        """ return None """
        return None

    @property
    def photo(self):
        """ return None """
        return None

