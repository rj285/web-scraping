import pandas as pd

df = pd.read_excel("romart.xlsx")

# print(df) 
"""     
     name   price  category
0   apple   1.25   fruits
1  orange   1.32   fruits
2  banana   1.85   fruits  """
index_row = df.iterrows()
for index , row in index_row:
    print("_________________________")
    print(index)
    print("-------------------------")
    print(row)
