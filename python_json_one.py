#import json 

import json

car_data = {"name": "tesla",
            "engine":"electric"}

print(car_data)
print(type(car_data)) # <class dict>

# json.dumps changes python dictionary to json string 

car_data_json_string = json.dumps(car_data)

print(type(car_data_json_string)) # returns <class string> 
# removes the need to cast data scraped from the web into specific data types 

# create a jsonfile with writing permissions 

with open("new_json_file.json","w") as jsonfile:
    json.dump(car_data, jsonfile)
    # ENCODING and writing into json file
    # "w" gives write permissions
    # the dump method takes two args : the first = dictionary, second = the jsonfile(fileobject)
    #"enter the name of the file", permission type

with open("new_json_file.json") as jsonfile:  # Decoding
    # Reading from the file we just created
    car = json.load(jsonfile)  # storing data from file to car variable
    print(type(car)) # Checking the type of the data again
    print(car['name']) # To get the value stored in key called name
    print(car['engine']) # To get the value of second key value pair

    