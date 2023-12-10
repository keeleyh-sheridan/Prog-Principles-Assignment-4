#functionality required to create, read, update, and delete a resource.   

import random
import Data_Persistence as file_data

#Append an item to the json
def add(item):
    new_file = file_data.load_file()
    new_file.append(item)
    file_data.save_file(new_file)

#Remove an item from the json
def remove(index):
    new_file = file_data.load_file()
    new_file.pop(index)
    file_data.save_file(new_file)

#Replace an item in the json at a specified index
def update(index, new_item):
    new_file = file_data.load_file()
    new_file[index] = new_item
    file_data.save_file(new_file)

#Find the index of an item in Resource json and return it
def search_index(ID):
    new_file = file_data.load_file()

    for item in new_file:
        if ID == item["ID"]:
            return new_file.index(item)
    return -1

#Generate a unique 3 digit number that is no shared by any other items
def generate_id():
    new_file = file_data.load_file()

    all_ids = ""
    for item in new_file:
        all_ids += f" {item['ID']}"

    ID = str(random.randint(100,999))
    while ID in all_ids:
        ID = str(random.randint(100,999))

    return ID

#Return a formatted string containing relevent item information as well as the dictionary object for the last searched item
def get_items(search_term):  
    new_file = file_data.load_file()

    info_string = ""
    item_dict = {}

    #Nested loop that checks every value in each dictionary contained by the json for key words that match the user inpu
    for item in new_file:
        if search_term.lower() == "all":
            info_string += f"\n{item['name']} {item['type']} pedal: {item['parameters']} ID: {item['ID']}"
        else:
            for key, value in item.items():
                if key == "parameters":
                    for list_item in value:
                        if list_item in search_term.lower():
                            if item["ID"] not in info_string:
                                info_string += f"\n{item['name']} {item['type']} pedal: {item['parameters']} ID: {item['ID']}"
                                item_dict = item
                else:
                    if str(value).lower() in search_term.lower():
                        if item["ID"] not in info_string:
                            info_string += f"\n{item['name']} {item['type']} pedal: {item['parameters']} ID: {item['ID']}"
                            item_dict = item
                    
    return info_string, item_dict
