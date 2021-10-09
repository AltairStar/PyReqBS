import requests
from bs4 import BeautifulSoup
class Coinmarketcap:

    def __init__(self, name):
        self.name = name

    def get_info(self,name="default"):
        if name == "default":
            name = self.name
        print(name)

        url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(name)

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')

        print(soup.find_all('p'))
