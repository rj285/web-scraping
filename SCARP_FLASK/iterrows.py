import pandas as pd

data = {'name':['sanjay','yasin','arya'],
        'age':[25,40,85],
        'city':["pattambi","balussery","ulliyeri"]}
# print(data)

df = pd.DataFrame(data)
# print(df)

for index, row in df.iterrows():
    print("Index",index)
    print("Rowdata: ")
    print(row)
    print()
