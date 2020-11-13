import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

# Data types

#1 - type of particular columns
type_desc= reviews.description.dtype
type_price= reviews.price.dtype
#print(type_desc, type_price, sep='\n')

#2 - types in entire DataFrame
type_all= reviews.dtypes
#print(type_all)

#3 - casting/converting
int_to_float= reviews.points.astype('float64')
#print(int_to_float)

#4 - type of DataFrame/Series index
index_type= reviews.index.dtype
# print(index_type)


# Missing Data

#1 - retrieving missing data
missing_data_country= reviews[pd.isnull(reviews.country)]
# print(missing_data_country)

#2 - replacing missing values
replace_nan_rediogn_2= reviews.region_2.fillna("Unknow")
#print(replace_nan_rediogn_2)

#3 - backfill strategy -> fill each missing value with the first non-null value
#    that appears sometime after the given record in the database

#4 - replace() method
taster_replaced= reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(taster_replaced)
