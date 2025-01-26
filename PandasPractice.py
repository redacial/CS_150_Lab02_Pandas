import pandas as pd
#
# s = pd.Series([42, 35, 6, 17])
# print(s)

df = pd.DataFrame({'age': 18, 'name': ['Alice', 'Carl', 'Bob'], 'cardio': [60, 70, 80]})

# print(df)

# print(df['age'])

df['age'] = 21

print(df)
