# TOPIC 1
# its like python dictionary {key:value}, but just a *string of text*

# Python dictionary :   lives inside Python program (can manipulate)
# JSON string       :   just text, used for sending/storing data between systems

#json.dumps() - Python dict -> JSON string
import json

##person = {"name": "yudi", "age": 22}

##json_string = json.dumps(person)
##print(json_string)
##print(type(json_string))

# ^dumps = "dump to string". The result not a dict, but a string

#json.loads() - JSON string -> Python dict
##json_string = '{"name": "yudi", "age": 22}'

##person = json.loads(json_string)
##print(person["name"])
##print(type(person))

# ^load = string to Python dict

#json.dump() - write JSON to a file
##person = {"name": "yudi", "age": 22}

##with open("person.json", "w") as f:
##    json.dump(person, f)

# ^save dictionary as JSON file to dictionary, for storing data

##with open("person.json", "r") as f:
##    person = json.load(f)

##print(person['name'])

# ^reads json file back into a Python dictionary

me = {"name": "yudi", "age": 22, "city": "Malang", "hobbies": "gym"}

json_string = json.dumps(me)
print(json_string)  