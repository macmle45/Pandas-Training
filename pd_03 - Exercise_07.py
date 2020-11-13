import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

def translate_rating_points(row):
    points= row.points
    if (row.country == "Canada" or points >= 95):
        points= 3
        return points
    elif (points >= 85 and points < 95):
        points= 2
        return points
    else:
        points= 1
        return points

star_ratings= reviews.apply(translate_rating_points, axis='columns')

print(star_ratings, star_ratings.describe(), sep='\n\n')
