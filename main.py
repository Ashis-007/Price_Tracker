from bs4 import BeautifulSoup
import requests


class Product():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price():
        return self.__price

    def set_price(price):
        self.__price = price

    def get_name():
        return self.__name


my_url = "https://www.banggood.in/Motor-Driver-Shield-L293D-Duemilanove-Mega-U-NO-p-72855.html?rmmds=search&cur_warehouse=CN"

req = requests.get(my_url)
print(req)

with open("index.html", "wb") as file:
    file.write(req.text.encode())

soup = BeautifulSoup(req.text, "lxml")

product_name = soup.find_all("class=title_strong")
print(product_name)
