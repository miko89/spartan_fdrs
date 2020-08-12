import pandas as pd

df = pd.DataFrame({'x1': ['206', '226', '245',' 265', '283'],
                    'x2': ['214', '234', '253', '272', '291']})

print(df)

df['x2'] = df['x2'].shift(-1)

print(df)
