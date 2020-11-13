import pandas as pd

reviews= pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)

# Renaming

#1 - rename column
print(reviews.rename(columns={'points': 'score'}))

#2 - rename index
print(reviews.rename(index={0: 'first', 1: 'second'}))

#3 - axis names
axis_names= reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(axis_names)


# Combining - concat(), join(), merge()

canadian_youtube= pd.read_csv("SampleData/YouTubeData/CAvideos.csv")
british_youtube= pd.read_csv("SampleData/YouTubeData/GBvideos.csv")

#1 - concat
concatenated_df= pd.concat([canadian_youtube, british_youtube])
print(concatenated_df)

#2 - join
left= canadian_youtube.set_index(['title', 'trending_date'])
right= british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

print(left)
