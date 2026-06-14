import pandas as pd

data = {
    'name': ['Hamilton', 'Verstappen', 'Leclerc', 'Norris', 'Sainz', 'Russell', 'Perez'],
    'points': [245, 289, 198, 212, 178, 165, 150],
    'team': ['Ferrari', 'Red Bull', 'Ferrari', 'McLaren', 'McLaren', 'Mercedes', 'Red Bull'],
    'wins': [3, 7, 2, 4, 1, 2, 0]
}

df = pd.DataFrame(data)
print('Driver Standings')
print(df)

#Task 1- Drivers with more than 2 wins
print('\n2 Wins or More')
print (df[df['wins']>2]) 

#Task 2- Total points scored by all drivers combined
print('\nTotal Points Combined')
print (df['points'].sum())

#Task 3- Average wins per team
print('\nAverage Wins per Team')
print (df.groupby('team')['wins'].mean())

#Task 4-Win rate per driver
print('\nWin Rate per Driver')
df['win_rate']=(df['wins']/df['points']*100)
print(df)

#Task 5- DataFrame sorted by win rate from highest to lowest
print('\nWin Rate - Highest to Lowest')
print(df.sort_values(by='win_rate', ascending=False))