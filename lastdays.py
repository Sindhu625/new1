import requests

all = input("Enter an input:")

res = requests.get(f"https://disease.sh/v3/covid-19/historical/all?lastdays={all}")

data = res.json()

#all = data['all']

for data in data:
    print(data['all'])                                                  