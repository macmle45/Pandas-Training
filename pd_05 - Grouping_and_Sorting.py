import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

#Groupwise analysis

#1
numb_of_marks_per_taster= reviews.groupby('taster_name').taster_name.count()
#print(numb_of_marks_per_taster)

#2
lowest_price_in_points_groups= reviews.groupby('points').price.min()
#print(lowest_price_in_points_groups)

#3
first_wine_from_winery_groups= reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
#print(first wine from winery groups)

#4
best_by_country_province= reviews.groupby(['country', 'province']).apply(
                            lambda df:
                                df.loc[df.points.idxmax()]
                        )
#print(best_by_country_province)

#5
points_stats_by_country= reviews.groupby('country').points.agg([min, max, 'mean', 'count'])
#print(points_stats_by_country)


#Sorting

#1 - ascending default | it's possible to sort by more than one column
print(points_stats_by_country.sort_values(by=['count', 'mean'], ascending=False))
