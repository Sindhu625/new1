import requests

sd = input('Enter start date:')
ed = input('Enter end date:')
mag = input('Enter magnitude:')

res = requests.get(f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={sd}&endtime={ed}&minmagnitude={mag}")

data = res.json()

features = data['features']

for feature in features:
    print(feature['properties']['mag'],feature['properties']['place'])