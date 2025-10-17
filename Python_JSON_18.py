# Convert from JSON to Python
import json

x= '{"Name":"Taofick","Age":24}'
y=json.loads(x)

print(y["Age"])



# Convert from Python to JSON
import json

x={
    "name":"taofick",
    "age":30,
    "city":"Comilla"
}

y=json.dumps(x)
print(y)




# Convert a Python object containing all the legal data types
import json

x={
    "name":"Taofick",
    "age":24,
    "Married":False,
    "childern":None,
    "Car":[
        {"model":"Bmw 230","color":"Red"},
        {"model":"ford","color":"Black"}
    ]
}
print(json.dumps(x,indent=2))



# Convert a Python object containing all the legal data types

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))