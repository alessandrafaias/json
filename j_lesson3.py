''' Javascript Object Notation'''
'''grabbing json data from public API'''
#https://docs.python.org/3/library/json.html
#https://www.youtube.com/watch?v=9N6a-VLBa2I&t=6s
#É um formato de dados muito comum para armazenar algumas informações.

import json
#makes request to the web API
from urllib.request import urlopen

#urlopen is a function
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

#data = json.loads(source)

#print(json.dumps(data, indent=2))

#confirms if there is really 188 resources in the list
#print(len(data['list']['resources']))

#let's make a convertion of dollars
usd_rates = dict()

for item in data['list']['resources']:
    #print(item)
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price
#print(usd_rates['USD/EUR'])

#converting 50 dollars to euros
print(50 * float(usd_rates['USD/EUR']))