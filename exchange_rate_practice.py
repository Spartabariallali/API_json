# method to return the exchange rates
car_data = {"name":"tesla","engine":"electric"}
# json.dumps() changes a python dictionary into a json string
# create a new variable for the json string as example below 
car_data_json_format = car_data.json.dumps()
# to verify if the new variable is in json format check with type()
print(type(car_data_json_format)