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

def search():
    pass