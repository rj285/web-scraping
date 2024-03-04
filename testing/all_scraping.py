from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def HOME():
    return 'PRICE INTELLIGENCE SOFTWARE IS UP AND RUNNING....'

#SPROUTS
@app.route('/api/v1/getS/<category>/<item>')
def getS(category,item):
    
    with open("config/cl.json",'r') as file:
        competitor = json.load(file)['S']
    
    URL = f"{competitor['store_api']}{category}/{item}"
    
    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
        }    
    
    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()
    items = data['items']
    
    for i in items:
        categories = i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict['name'].lower())
                if item in i['name'].lower():
                    item_found = {
                        "name":i['name'],
                        "price":i['base_price']
                    }
    return ({"items":item_found})



#WEGMANS
@app.route('/api/v1/getW/<category>/<item>')
def getW(category,item):
    
    with open("config/cl.json",'r') as file:
        competitor = json.load(file)['W']
    
    URL = f"{competitor['store_api']}{category}/{item}"
    
    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
        }    
    
    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()
    items = data['items']
    
    for i in items:
        categories = i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict['name'].lower())
                if item in i['name'].lower():
                    item_found = {
                        "name":i['name'],
                        "price":i['base_price']
                    }
    return ({"items":item_found})

#THE FRESH MARKET
@app.route('/api/v1/getT/<category>/<item>')
def getT(category,item):
    
    with open("config/cl.json",'r') as file:
        competitor = json.load(file)['T']
    
    URL = f"{competitor['store_api']}{category}/{item}"
    
    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie':competitor['cookie']
        }    
    
    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()
    items = data['items']
    
    for i in items:
        categories = i['categories']
        for category_dict in categories:
            if category in category_dict['name'].lower():
                print(category_dict['name'].lower())
                if item in i['name'].lower():
                    item_found = {
                        "name":i['name'],
                        "price":i['base_price']
                    }
    return ({"items":item_found})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
