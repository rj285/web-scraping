import pandas as pd
import requests
import json

with open("cl.json",'r') as file:
    competitor = json.load(file)
    
search_term = str(input("Enter the name to search:- "))
    
URL = competitor['sprouts']['store_api'] + search_term
    
HEADERS = { 
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':competitor['sprouts']['cookie']
}    
    
responses = requests.get(URL, headers=HEADERS)
data = responses.json()

item_found = []
if 'items' in data:
    items = data['items']
    for item in items:
        name = item.get('name')
        price = item.get('base_price')
        category = item.get('categories')
        for cats in category:
            # if "produce" in cats['name'].lower():
                category_name = cats.get('name')
                item_found.append({"name": name, "price": price, "categories": category_name})
        
df = pd.DataFrame(item_found)
# for index, row in df.iterrows():
#     print("_______________________________")
#     print(index)
#     print("-------------------------------")
#     print(row)
df.to_excel("romart.xlsx", index=False)