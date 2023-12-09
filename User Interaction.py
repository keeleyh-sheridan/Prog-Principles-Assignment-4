import Resource_Manager as rm

#interaction with the user

def menu():
    while True:
        print('''
-----------------------
1. Create
2. Read(Search)
3. Edit
4. Delete
5. Exit
-----------------------''')
        
        option = input("Choose an option from the menu: ")
        if option == "1":
            create_pedal()
        elif option == "2":
            read()
        elif option == "3":
            edit()
        elif option == "4":
            delete()
        elif option == "5":
            print("Thank you for using this pedalboard manager! Exiting....")
            exit()
        else:
            print("Invalid option selected")

def create_pedal():
    item = {}
    item["name"] = input("Enter the name of added guitar pedal: ")
    item["type"] = input("Enter the kind of guitar pedal: ")
    
    parameters = []
    while True:
        new_parameter = input("Enter a parameter that the pedal has. If all parameters have been added type 'done': ")
        
        if new_parameter.lower() == "done":
            break

        parameters.append(new_parameter.lower())
    item["parameters"] = parameters

    item["ID"] = rm.generate_id()

    rm.add(item)
    print(f"The pedal has been added and has unique ID number: {item['ID']}")
    
def read():
    print(rm.get_items(input("Enter one or more attributes (in the same line) or enter 'all' to read all items: "))[0])

def edit():
    ID = input("Enter the ID of the item you would like to edit: ")
    index = rm.search_index(ID)

    if index == -1:
        print("ID invalid, item not found")
        return
    
    info_string, edit_pedal = rm.get_items(ID)

    print(f"You are editing: {info_string}")

    while True:
        for key, value in edit_pedal.items():
            if key == "ID":
                continue

            change_val = "t"
            while change_val not in "yn":
                change_val = input(f"The {key} of the pedal is {value}. Would you like to edit this?(y/n) ").lower()
            if change_val == "y":
                if key == "parameters":
                    parameters = []
                    while True:
                        new_parameter = input("Enter a parameter that the pedal has. If all parameters have been added type 'done': ")
                        
                        if new_parameter.lower() == "done":
                            break

                        parameters.append(new_parameter.lower())
                    edit_pedal["parameters"] = parameters
                else:
                    edit_pedal[key] = input("What would you like the new value to be? ")

        print(f"The updated pedal is: {edit_pedal['name']} {edit_pedal['type']} pedal: {edit_pedal['parameters']} ID: {edit_pedal['ID']}\n")
        change_val = "t"
        while change_val not in "yn":
            change_val = input("Would you like to make more changes?(y/n) ").lower()
            if change_val == "n":
                rm.update(index, edit_pedal)
                return

def delete():
    index = rm.search_index(input("Enter the ID of the item you would like to delete: "))

    if index == -1:
        print("ID invalid, item not found")
    else:
        rm.remove(index)

menu()