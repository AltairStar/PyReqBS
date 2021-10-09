import sys
sys.path.append('../src/Coin.py')
from src import Coin

scrapper  = Coin.Coinmarketcap('xrp')#default param

scrapper.get_info()#default is initialization param in class

scrapper.get_info("bitcoin")#use another param