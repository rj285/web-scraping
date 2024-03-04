import pandas as pd

data = {"a":['apple','banana','orange'],
        "b":['cat','dog','bird'],
        "c":['red','blue','green']}

# print(data)
df = pd.DataFrame(data)
# print(df.at[0,'a'])
# print(df.at[1,'b'])
# print(df.at[2,'c'])
# print(df)

op = pd.DataFrame(index=df.index,columns = ['a','b','c'])

for index , row in df.iterrows():
    for col in df.columns:
        op_df = df.at[index, col] = row[col]

op_df.to_excel("at.xlsx", index = False)




