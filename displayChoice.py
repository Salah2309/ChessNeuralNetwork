#This file will change the display to any chosen node!
import json
file = 'Frontend/Layout.json'

def editJson(file, data):
    try:
        with open(file, 'w') as file:
            json.dump({"imgs": data}, file, indent=4)
        print(f"Updated new data to '{file}'")
    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display(file):
    try:
        with open(file, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))  # Display the JSON data
            return data
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def getData():
    return[["BR","BN","BB","BQ","BK","BB","BN","BR"],["BP","BP","BP","BP","BP","BP","BP","BP"],["-","-","-","-","-","-","-","-"],
           ["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],["-","-","-","-","-","-","-","-"],
           ["WP","WP","WP","WP","WP","WP","WP","WP"],
           ["WR","WN","WB","WQ","WK","WB","WN","WR"]]   


display(file)
editJson(file, getData())