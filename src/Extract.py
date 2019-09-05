import requests
from bs4 import BeautifulSoup

def Extract(products,url):
    request = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    element = soup.findAll("span",{"class": "title"})
    for product in element:
        fixstring = ''.join(char for char in product.text if ord(char) < 128)
        products.add_product(fixstring)

    element = soup.findAll("div", {"class":"search_price"})
    for product in element:
        price = product.text
        count = 2
        control = 0
        while (control == 0):
            if price[count] == '$':
                control = 1
            count += 1
        products.add_price(price[count:])