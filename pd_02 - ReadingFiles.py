import pandas as pd

#Reading data files

lego= pd.read_csv("C:/Users/milkm/Desktop/archive/metadata.csv", index_col= 0)



print(lego.shape, lego, sep='\n')
