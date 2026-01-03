import requests

year = input('Enter a year:')

res = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e=Arsenal_vs_Chelsea&s={year}")

data = res.json()

#teams = data['teams']

if data.get("event"):
    for event in data["event"]:
        print("Season:", event.get("strSeason"))
        print("Event:", event.get("strEvent"))
        print("Date:", event.get("dateEvent"))