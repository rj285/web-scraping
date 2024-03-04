from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/')
def HOME():
    return 'H O M E _ P A G E'

@app.route('/api/v1/getsprouts/<item>')
def getsprouts(item):
    with open("config/cl.json",'r') as file:
        competitor = json.load(file)['S'] 
        
    url = f"{competitor['store_api']}{item}" 

    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': competitor['cookie']
        }

    responses = requests.get(url,headers=HEADERS)
    data = responses.json()
    return data['items'][0]['name']

if __name__ == "__main__":
    app.run(debug=True)