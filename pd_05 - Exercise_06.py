import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

res= reviews.groupby(['country', 'variety']).points.max()

res.sort_values(by='max', ascending=False)

print(res)
