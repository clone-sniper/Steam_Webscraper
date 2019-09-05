from src.Extract import Extract
from src.Item import Item
from src.StoreData import StoreData

url = "https://store.steampowered.com/search/?filter=topsellers&specials=1"
products = Item()
Extract(products,url)
x = 0
while(x < len(products.name)):
    print(products.name[x] + " " + products.price[x])
    x+=1
StoreData(products)