drivers=[
    {"name": "Hamilton", "points": 245, "team": "Ferrari"},
    {"name": "Verstappen", "points": 289, "team": "Red Bull"},
    {"name": "Leclerc", "points": 198, "team": "Ferrari"},
    {"name": "Norris", "points": 212, "team": "McLaren"},
    {"name": "Sainz", "points": 178, "team": "McLaren"}
]
     
def find_leader(drivers):
    leader=drivers[0]
    for driver in drivers:
        if driver["points"] > leader["points"]:
            leader=driver
    return leader["name"]

print(find_leader(drivers))

def print_standings(drivers):
   for driver in drivers:
       print (f"{driver['name']} | {driver['team']} | {driver['points']}")

print_standings(drivers)


def average_points(drivers):
    total=0
    for driver in drivers:
        total+=driver["points"]
    average= total/len(drivers)
    print(f"{average:.1f} points")
    return(average)


average_points(drivers)

def sorted_standings(drivers):
   sorted_drivers=sorted(drivers, key=lambda driver: driver["points"], reverse=True)
   for driver in sorted_drivers:
       print (f"{driver['name']:<10} | {driver['team']:<9} | {driver['points']} points")

sorted_standings(drivers)
