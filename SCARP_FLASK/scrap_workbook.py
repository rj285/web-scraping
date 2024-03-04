from flask import Flask
import json
import requests
from openpyxl import Workbook

app = Flask(__name__)

def item_parser(category, search_term, site):
    try:
        with open("config/cl.json",'r') as file:
            competitor = json.load(file)[site]
    except:
       return ({
           "site": site,
           "status": 404,
           "message": f"The server received your request, but the requested resource for {site}/{category}/{search_term} could not be located."
           })

    URL = f"{competitor['store_api']}{category}/{search_term}"
    HEADERS = { 
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': competitor['cookie']
    }
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if 'items' in data:
        items = data['items']
        for item in items:
            categories = item['categories']
            for category_dict in categories:
                if category in category_dict['name'].lower() and search_term in item['name'].lower():
                    item_found = {
                        "name": item['name'],
                        "price": item['base_price'],
                        "website": site  # Adding website name to the item_found dictionary
                    }
                    return item_found 
            return None
        return ({
            "status": 404,
            "message": f"The requested items for {search_term} in {category} category at {site} were not found."
            })

#http://127.0.0.1:5000/api/v1/getitem/sprouts/fruits/apple
@app.route('/api/v1/getitem/<site>/<category>/<search_term>')
def get_item(category, search_term, site):
    item = item_parser(category, search_term, site)
    if item:
        # Creating an Excel file
        wb = Workbook()
        ws = wb.active
        ws.title = "Item Data"
        ws.append(["Website", site])  
        ws.append([item["name"], item["price"]])
        filename = f"{search_term}.xlsx"
        wb.save(filename)
        return f"Data saved to {filename} from {site}"
    else:
        return "Item not found"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

