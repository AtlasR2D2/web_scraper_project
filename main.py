# Coronavirus WFH Survival Guide

import requests
from bs4 import BeautifulSoup

webpage_URL = "https://johnlefevre.medium.com/your-coronavirus-wfh-survival-guide-424d4ce3dc5e"

response = requests.get(webpage_URL)

soup = BeautifulSoup(response.content,features="lxml")

article_headers = soup.find_all("h1")

article_bodies = soup.find_all("p", class_="ka")

list_header = article_headers[0].text

item_headers = []
header_id = 0

for header in article_headers:
    if header_id > 0:
        item_headers.append(header.text)
    header_id += 1

item_bodies = []
for body in article_bodies:
    item_bodies.append(body.text)

# Add an additional blank entry for the last item
item_bodies.append("Nuff said.")

items = dict(zip(item_headers,item_bodies))

# Show the survival guide list
print(list_header)
print("\n")
for key, value in items.items():
    print(f"{key}")
    print(f"{value}")
    print("\n")