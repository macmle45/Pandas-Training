import pandas as pd

#Reading data files

lego= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col= 0)



print(lego.shape, lego, sep='\n')
