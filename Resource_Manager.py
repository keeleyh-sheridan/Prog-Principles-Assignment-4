#functionality required to create, read, update, and delete a resource.   

import Data_Persistence as file_data

def add(item):
    new_file = file_data.load_file()

    new_file.append(item)

    file_data.save_file(new_file)

def remove(index):
    new_file = file_data.load_file()

    new_file.pop(index)

    file_data.save_file(new_file)

def update():
    pass

def search(search_term):
    new_file = file_data.load_file()

    for item in new_file:
        for info in item:
            if search_term == info:
                return new_file.index(item)


def get_items(search_term):  
    new_file = file_data.load_file()

    info_string = ""
    for item in new_file:
        if search_term.lower() == "all":
            info_string += f"{item['name']} {item['type']} pedal: {item['parameters']}\n"
        else:
            for key, value in item.items():
                try:
                    if value.lower() in search_term.lower():
                       info_string += f"{item['name']} {item['type']} pedal: {item['parameters']}\n"
                except TypeError:
                    for list_item in value:
                        if list_item.lower() in search_term.lower():
                            info_string += f"{item['name']} {item['type']} pedal: {item['parameters']}\n"
    return info_string
