import pandas as pd

#Reading data files

wines= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col= 0)
pd.set_option('max_rows', 20)


print(wines.shape)


#Indexing in Pandas

#Index-based selection paradigm (iloc - exclusive)
wines_part = wines.iloc[-5:] #last five positions in csv file
wines_part.to_csv('wines_part.csv') #saving DataFrame object to csv file called 'wines_part.csv'

print(wines_part)

#Label-based selection paradigm (loc - inclusive)
wines_part_2 = wines.loc[:5, ['country', 'points']]

print(wines_part_2)

#Manipulating the index
print(wines.set_index("title"))


#Conditional selection
wines_by_country= (wines.country == 'France') & (wines.points >= 90) #it produced Series object (True/False)

print(wines.loc[wines_by_country])

#Pandas built-in conditional selectors

#isin
print(wines.loc[wines.country.isin(['Italy', 'France'])])

#notnull
print(wines.loc[wines.price.notnull()])

#Pandas assigning data
wines['critics']= 'macmle'
print(wines['critics'])
