''' Javascript Object Notation'''
#https://docs.python.org/3/library/json.html
#https://www.youtube.com/watch?v=9N6a-VLBa2I&t=6s
#É um formato de dados muito comum para armazenar algumas informações.

import json

with open('C:/Users/user/Documents/Python/Python Corey/json/states.json') as f:
    data = json.load(f) 
#this is a method that loads a file int a python object / (json.loads loads a string)

#for state in data['states']:  #accessing states key
#    print(state['name'], state['abbreviation'])

#let's make another json file without area_codes key
for state in data['states']:
    del state['area_codes']

with open('C:/Users/user/Documents/Python/Python Corey/json/new_states.json', 'w') as f:
    json.dump(data, f, indent=2) #look at your directory. There is a new file there.

