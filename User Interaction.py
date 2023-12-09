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
        
        selection = input("Choose an option from the menu: ")
        if selection == "1":
            create_pedal()
        elif selection == "2":
            read()
        elif selection == "3":
            pass
        elif selection == "4":
            pass
        elif selection == "5":
            break

def create_pedal():
    item = {}
    item["name"] = input("Enter the name of added guitar pedal: ")
    item["type"] = input("Enter the kind of guitar pedal: ")
    
    parameters = []
    while True:
        new_parameter = input("Enter a parameter that the pedal has. If all parameters have been added type 'done': ")
        
        if new_parameter.lower() == "done":
            break

        parameters.append(new_parameter)
    item["parameters"] = parameters

    rm.add(item)
    
def read():
    print(rm.get_items(input("Enter one or more attributes (in the same line) or enter 'all' to read all items: ")))
    
def item_info():
    pass

menu()