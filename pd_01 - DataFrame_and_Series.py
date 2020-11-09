import pandas as pd

#Data Frame

exmpl_DF = pd.DataFrame(
    {
        'Product A': [24.99, 100],
        'Product B': [34.99, 50]
    },
    index= ['Price', 'Quantity']
    )

#print(exmpl_DF)

#Series

exmpl_S = pd.Series(
        [0, 1, 2, 3]
    ,
    name= 'Alphabet',
    index= ['A', 'B', 'C', 'D']
    )

print(exmpl_S)
