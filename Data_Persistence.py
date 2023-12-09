#code that is responsible with saving and loading resource data into / from files. 
import os.path
import json

def save_file(new_file):
    #if os.path.isfile("Resource.json"):
    with open("Resource.json", "w") as save_file:
        json.dump(new_file, save_file)

def load_file():
    with open("Resource.json", "r") as read_file:
        return json.load(read_file)