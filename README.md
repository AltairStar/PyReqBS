# BeautifulSoup and request usage
Language used:python\
Version:3.9\
#Class
Importing request and BeautifulSoup
```bash
import requests
from bs4 import BeautifulSoup
```
Creating class
```bash
class Coinmarketcap:
```
Creating the parametres to our class
```bash
def __init__(self, name):
  self.name = name
```
Creating method with attributes
```bash
def get_info(self,name="default"):
```
Giving to our attribute new value
```bash
def get_info(self,name="default"):

  if name == "default":
    name = self.name
```
Saving link of site with which we will work
```bash
def get_info(self,name="default"):

  if name == "default":
    name = self.name

  url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(name)
```
Using BeautifulSoup and request to find out the code of this site
```bash
def get_info(self,name="default"):
  if name == "default":
    name = self.name

  url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(name)

  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'html.parser')
```
Using method find_all to find out all information with this attribute, such as our code 'p'
```bash
def get_info(self,name="default"):
  if name == "default":
    name = self.name

  url = 'https://coinmarketcap.com/ru/currencies/{0}'.format(name)

  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'html.parser')

  print(soup.find_all('p'))
```





