import pandas as pd
df = pd.read_csv('international-airline-passengers.csv', engine='python', skipfooter=3)

print(df.columns)

df.columns = ['month', 'passengers']
print(df.columns)

print(df['passengers'])
print(df.passengers)

df['ones'] = 1
print(df.head())