#WebScraper works only with https://oz.by/ preferred to use with books.

import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


product_url = input("Enter url of the product: ")
r = requests.get(product_url)

soup = bs(r.text, "html.parser")

#TITLE

title = soup.find("h1",{"itemprop" : "name"})
print(f"Title: {title.text}")

#AUTHOR
try:
    author = soup.find("a",{"class" : "b-product-title__inner-link"})
    print(f"Author: {author.text}")
except:
    print("Author:None")
#PUBLISHER
try:
    dom = etree.HTML(str(soup))
    publisher = dom.xpath('//table/tbody/tr[8]/td[2]')[0].text
    print(f"Publisher:{publisher}")
except:
    print("Publisher: None")
#PRICE
price = dom.xpath('//*[@id="top-page"]/div[3]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/div/span/text()')[0]
price = price.strip()
print(f"Price: {price}")

#DESCRIPTION
description = dom.xpath('//div[@id = "truncatedBlock"]/p')[0].text

print(f"Description: {description}")

#COVER
soup = bs(r.content,'html.parser')
book_cover = soup.find("img",{"class":"lazy loaded"})['src']
print(f"Link for cover of the book: {book_cover}")
