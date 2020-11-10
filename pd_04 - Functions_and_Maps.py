import pandas as pd
pd.set_option('max_rows', 5)

import numpy as np

reviews = pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

#Pandas summary functions

#Function describe()
print(reviews.points.describe(), '\n')
print(reviews.taster_name.describe(), '\n')

#Statistical functions
print(reviews.points.mean(), '\n')
print(reviews.taster_name.unique(), '\n')
print(reviews.taster_name.value_counts(), '\n')


#Maps

#map() function - for data Series
review_points_mean = reviews.points.mean()
reviews_mapped= reviews.points.map(lambda p: p - review_points_mean)

print(reviews_mapped, '\n')

#apply() funtion - for DataFrames
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

#reviews_points_mapped= reviews.apply(remean_points, axis='columns')
#print(reviews_points_mapped)

#built-in
print(reviews.country + ' - ' + reviews.region_1)
