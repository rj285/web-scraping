from flask import Flask
import json
import requests
import pandas as pd

app = Flask(__name__)

def item_parser(site,category,search_term):
    try:
        with open("cl.json",'r') as file:
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
        'Cookie':competitor['cookie']
    }
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    if(data.get('items')):
        items=data.get('items')
        # items_df = pd.DataFrame(data.get('items'))
        for item in items:
            categories=item['categories']
            for category_dict in categories:            
                if category in category_dict['name'].lower():
                    if search_term in item['name'].lower():
                        item_found={
                                    "name":item['name'],
                                    "price":item['base_price'],
                                    }
                        status=200
                        break   
        return ({"status": status, "item": item_found})
    else:
        return ({
            "status": 404,
            "message": f"The requested items for {search_term} in {category} category at {site} were not found."
            })


@app.route('/api/v1/getitem/<site>/<category>/<search_term>')   
def getitem(site,category,search_term):
        return(item_parser(site,category,search_term))

if __name__ == '__main__':
    app.run(debug=True, port=8000)