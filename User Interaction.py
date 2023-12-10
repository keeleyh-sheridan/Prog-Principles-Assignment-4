import Resource_Manager as rm

#interaction with the user

#Main menu for user interaction
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

#Create a pedal dict object and return it to resource manager
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
    print(f"\nThe pedal has been added and has unique ID number: {item['ID']}")
    
#Print all pedals that match any terms submitted by the user
def read():
    print(rm.get_items(input("Enter one or more attributes (in the same line) or enter 'all' to read all items: "))[0])

#Edit a pedal and pass it to resource manager
def edit():
    #Find the pedal to edit
    ID = input("Enter the ID of the item you would like to edit: ")
    index = rm.search_index(ID)

    if index == -1:
        print("ID invalid, item not found")
        return
    
    info_string, edit_pedal = rm.get_items(ID)

    print(f"\nYou are editing: {info_string}\n")

    #Loop containing code for editing the dict object
    while True:
        for key, value in edit_pedal.items():
            #Don't edit the ID key
            if key == "ID":
                continue
            #Check if user wants to edit a value
            change_val = "t"
            while change_val not in "yn":
                change_val = input(f"The {key} of the pedal is {value}. Would you like to edit this?(y/n) ").lower()
            if change_val == "y":
                #Change value to new input
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

        print(f"\nThe updated pedal is: {edit_pedal['name']} {edit_pedal['type']} pedal: {edit_pedal['parameters']} ID: {edit_pedal['ID']}")
        change_val = "t"
        
        #Exit the loop if user is happy with changes
        while change_val not in "yn":
            change_val = input("Would you like to make more changes?(y/n) ").lower()
            if change_val == "n":
                rm.update(index, edit_pedal)
                print("Pedal has been updated")
                return

#Delete a pedal
def delete():
    index = rm.search_index(input("Enter the ID of the item you would like to delete: "))

    if index == -1:
        print("ID invalid, item not found")
    else:
        rm.remove(index)
        print("Removed successfully")

print('''
Welcome to my guitar pedalboard manager app!
Guitar pedals are devices that can change how an electric guitar sounds,
they all have different functionalities and parameters.
This app allows you to manage which ones are in your collection.\n''')
menu()