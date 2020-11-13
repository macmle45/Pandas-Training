import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)
res= reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

print(res)
