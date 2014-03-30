from amazonproduct import API
import re

class Amazon():

    def __init__(self, url, locale='us'):
        self.api = API(locale=locale)
        self.asin = self.__get_product_id(url)
        self.result = self.api.item_lookup(
            self.asin,
            ResponseGroup='ItemAttributes,Offers,Images'
        )
        try:
            self.item = self.result.Items.Item[0]
        except IndexError:
            self.item = None

    def __get_product_id(self, url):
        """ get a amazon asin number from url """
        compiled_pattern = re.compile("([A-Z0-9]{10})")
        search_result = compiled_pattern.search(url)
        try:
            return search_result.group(0)
        except IndexError:
            return None

    @property
    def title(self):
        """ return title of Item """
        return self.item.ItemAttributes.Title.text

    @property
    def price(self):
        """ return lowest price of Amazon Item """
        try:
            return self.item.OfferSummary.LowestNewPrice.FormattedPrice.text
        except AttributeError:
            return None

    @property
    def currency(self):
        """ return currency of Amazon Item """
        try:
            return self.item.OfferSummary.LowestNewPrice.CurrencyCode
        except AttributeError:
            return None

    @property
    def photo(self):
        """ return small Image of Amazon Item """
        try:
            return self.item.SmallImage.URL.text
        except AttributeError:
            return None





