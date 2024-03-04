# import pandas as pd
# import requests
# import json

# with open ("config/cl.json",'r') as file:
#     competitor = json.load(file)

#     HEADERS = { 
#         'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
#         'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
#         'Cookie': competitor['cookie']
#     }
    
# df_romart = pd.read_excel("PIS/romart.xlsx",sheet_name="Sheet1")
# for i in range(0,len(df_romart)):
#     search_term = df_romart.loc[i]['name']
    
#     URL = f"{competitor['sprouts']['store_api']}{search_term}"

#     responses = requests.get(URL,headers=HEADERS)
#     data = responses.json()


#     items=data['items']
#     df_items = pd.DataFrame(items)
#     df_cleaned = df_items[['name','base_price','display_uom','average_weight']]

#     df_cleaned.to_excel(f"scrapies/{search_term}.xlsx",index=False)