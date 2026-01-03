import requests

drink = input('Enter a drink:')

res = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={drink}")

data = res.json()

#drinks = data['drinks']

if data.get("drink"):
    for item in data["drink"]:
        print("Drink Name:", item.get("strDrink"))
        print("Category:", item.get("strCategory"))
        print("Glass:", item.get("strGlass"))
