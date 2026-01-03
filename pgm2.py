import requests

word = input('Enter a word:')

res = requests.get(f" https://api.datamuse.com/words?sl={word}")

data = res.json()

#words = data['words']

for data in data:
    print(data['word'])