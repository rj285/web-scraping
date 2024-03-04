from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def HOME():
    return 'price intelligence software is up and running'

@app.route('/api/v1/gettfm/<category>/<item>')
def gettfm(category,item):

    with open("congig/cl.json",'r') as file:
        competitor = json.load(file)['tfm']  
           
    URL = f"{competitor['store_api']}{category}/{item}"
    
    HEADERS = {     
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie':competitor['cookie']
}
    
    response = requests.get(URL,headers=HEADERS)
    data = response.json()
    items=data["items"]
    
    for i in items:
        categories=i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict["name"].lower())
                if item in i['name'].lower():
                    item_found={
                        "name": i['name'],
                        "price":i['base_price']
                    }
    return ({"items":item_found})

if __name__ == '__main__':
    app.run(debug=True, port=8000)