import pandas as pd

reviews = pd.read_csv("SampleData/winemag-data-130k-v2.csv", index_col=0)
tropical= reviews.description.map(lambda desc: 'tropical' in desc).sum()
fruity= reviews.description.map(lambda desc: 'fruity' in desc).sum()

"""
def check_desc(row):
    desc= row.description
    if ('tropical' in desc) and ('fruity' in desc):
        return 2
    elif ('tropical' in desc) or ('fruity' in desc):
        return 1
    else:
        return 0
"""

#descriptor_counts= (reviews.apply(check_desc, axis='columns')).sum()

descriptor_counts= pd.Series(
     [tropical, fruity],
     index= ['Tropical', 'Fruity']
)

print(descriptor_counts)
