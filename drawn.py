from urllib import urlopen
from shop.amazon import Amazon
from shop.other import Other
import re
from django.utils.encoding import force_text

class Drawn:

    def __init__(self, url):

        self.url = self.__check_url(url)
        if 'amazon.co.uk' in self.url:
            self.item = Amazon(url, locale='uk')
        elif 'amazon.com' in self.url:
            self.item = Amazon(url, locale='us')
        elif 'amazon.it' in self.url:
            self.item = Amazon(url, locale='it')
        elif 'amazon.jp' in self.url:
            self.item = Amazon(url, locale='jp')
        elif 'amazon.fr' in self.url:
            self.item = Amazon(url, locale='fr')
        elif 'amazon.ca' in self.url:
            self.item = Amazon(url, locale='ca')
        elif 'amazon.de' in self.url:
            self.item = Amazon(url, locale='de')
        else:
            self.item = Other(url)

    def __check_url(self, url):
        """ check url in services """
        regex = re.compile(
            r'^(?:http)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if not regex.search(force_text(url)):
            raise ValueError('Not a URL')
        else:
            return url



