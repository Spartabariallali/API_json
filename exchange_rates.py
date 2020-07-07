import json

class Fetch_Data:
    def fetching_data():
        with open("exchange_rates.json","r") as exchange_rate_file:
            dataset = json.load(exchange_rate_file)
            for key in dataset:
                if key in dataset:
                    print(dataset["rates"])
        currency = input("\n which currency rate would you like to view: ").upper()
        print(dataset["rates"][currency])
    
fetch1 = Fetch_Data

fetch1.fetching_data() 









