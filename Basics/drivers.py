import pandas as pd

drivers=[
    {"name": "Hamilton", "points": 245},
    {"name": "Verstappen", "points": 289},
    {"name": "Leclerc", "points": 198},
    {"name": "Norris", "points": 212},
]

df=pd.DataFrame(drivers)
print(df)
