''' Javascript Object Notation'''
#https://docs.python.org/3/library/json.html
#https://www.youtube.com/watch?v=9N6a-VLBa2I&t=6s
#É um formato de dados muito comum para armazenar algumas informações.

import json #standard library

people_string = '''
{
    "people": [ 
        {
            "name": "Alessandra Faias",
            "phone": "55 11 94229-3371",
            "email": ["alles.faneco@gmail.com"],
            "has_license": false
        },
        {
            "name": "Allezi Faias",
            "phone": "55 11 97400-5134",
            "email": null,
            "has_license": true
        }
    ]
}
'''
#json key = people (line 6)
#value of people = array of more objects (lines 7 to 18)
#the value of people is an array of two objects. Each object has a key of name, phone, email and has_license

#loads into Python from a string (transforms a string into a python object)
#json.loads (load s) is a method from json library
data = json.loads(people_string)

#print(data)
#print(type(data)) #data is a dict type class
#print(type(data['people'])) #people is a list type class

#as people_string is a dictionary, we should be able to access the people key, because it's a list

#access the names of each person
#for person in data['people']:
#    print(person['name'])


for person in data['people']:
    del person['phone'] #deletes phone key
    #print(person)
#dump all back into a string
new_string = json.dumps(data, indent=2, sort_keys=True)
#indent like a json file. For each level it indents it twice / sort the keys with sort_keys argument. Makes even easier to read
print(new_string)

#json.loads() takes in a string and returns a json object.
#json.dumps() takes in a json object and returns a string.

