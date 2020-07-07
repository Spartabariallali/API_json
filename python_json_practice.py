import json

# method to return the exchange rates
car_data = {"name":"tesla",
            "engine":"electric"}

# json.dumps() changes a python dictionary into a json string
# create a new variable for the json string as example below 
car_data_json_format = json.dumps(car_data)
# to verify if the new variable is in json format check with type()
print(type(car_data_json_format)) # the output of this code returns a string 

############################################################################################################################

# the following code follows how we can open a json file from a python workspace 

# this code allows us to create a new json file - "name_of_file","permissions" either "w"/"r"
with open("json_file","w") as json_file_car_data:
    # uses the car_data dictionary above and enocdes it into the new aliased file 
    json.dump(car_data,json_file_car_data) 

# to ENCODE the data repeat steps above but remove permission 
with open("json_file") as json_file_car_data:
    # create a variable to contain the json data to be accessed by python 
    car = json.load(json_file_car_data)


print(car["name"])
print(car["engine"])