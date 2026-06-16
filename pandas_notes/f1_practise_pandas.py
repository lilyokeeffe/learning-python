import pandas as pd

data = {
    'name': ['Hamilton', 'Verstappen', 'Leclerc', 'Norris', 'Sainz', 'Russell', 'Perez'],
    'team': ['Ferrari', 'Red Bull', 'Ferrari', 'McLaren', 'McLaren', 'Mercedes', 'Red Bull'],
    'points': [245, 289, 198, 212, 178, 165, 150],
    'wins': [3,7,2,4,1,2,0]
}

df=pd.DataFrame(data)

#Task 1 - Full dataframe
print("===Full DataFrame===")
print(df)

#Task 2 - PName and Points Columns Only
print("\n===Name and Points===")
print(df[['name', 'points']])

#Task 3 - Ferrari Drivers Information Only
print("\n===Ferrari Drivers Only===")
print(df[df['team']=='Ferrari'])

#Task 4 - Driver with the Most Wins
print("\n===Most Wins===")
print(df[df['wins']==df['wins'].max()])

#Task 5 - Number of Points per Win
print("\n===Points per Win===")
df['points per win']=df['points']/df['wins']
print(df)

#Task 6 - Sort Teams by Average No. Points
print("\n===Average Points per Team===")
print(df.groupby('team')['points'].max())