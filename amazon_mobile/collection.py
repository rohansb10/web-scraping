import pandas as pd
from bs4 import BeautifulSoup

products = []
for i in range(1,247):  # check in data file how many html files created
    with open(f"./amazon_mobile/data/mobile_{i}.html", "r", encoding="utf-8") as file:
        # check the html file name
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    for card in soup.find_all("div", class_="puisg-col-inner"):
        title = card.find("span", class_="a-size-medium a-color-base a-text-normal").text if card.find("span", class_="a-size-medium a-color-base a-text-normal") else None
        price = card.find("span", class_="a-offscreen").text if card.find("span", class_="a-offscreen") else None
        rating = card.find("span", class_="a-icon-alt").text if card.find("span", "a-icon-alt") else None
        offer = card.find("span", class_="a-badge-text").text if card.find("span", "a-badge-text") else None
        
        if title and price :
            products.append({
                "Title": title, "price":price,"rating":rating,"offer":offer
            })

df = pd.DataFrame(products)
df.drop_duplicates()
df.to_csv("./amazon_mobile/products.csv", index=False)
df.shape