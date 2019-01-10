from onto_lib.onto_functions import *
import os
import types

cont = "y" #breaking var

#define script operations
def load_operations():
	operation = int(input("""
Please select an operation:
	1) List classes
	2) List object properties
	3) List individuals
	4) List data properties
	5) Insert new class
	6) Insert new individual
	7) Delete an entity
	>> """))
	return operation

#Switch script operations
def handle_operations(option, onto):
    option = int(option)
    if option == 1:
        try:
            list_classes(onto)
        except:
            print("Cannot list classes!")
    elif option == 2:
        try:
            list_rels(onto)
        except:
            print("Cannot list object properties!")
    elif option == 3:
        try:
            list_indv(onto)
        except:
            print("Cannot list individuals!")
    elif option == 4:
        try:
            list_data_properties(onto)
        except:
            print("Cannot list data properties!")
    elif option == 5:
        try:
            insert_class(onto)
        except:
            print("Cannot insert Class!")
    elif option == 6:
        try:
            insert_indv(onto)
        except:
            print("Cannot insert Class!")
    elif option == 7:
        try:
            delete_onto_entity(onto)
        except:
            print("Cannot finish the operation")
    else:
        print("Unknown operation!")
#App name
print("Ontology browser 1.0")

ont_path = str(input("Please enter the ontology path: "))

#check if the path exists 
if os.path.isdir(ont_path) == False:
	print("The given directory doesn't exist")
else:
	print("Path found (500)")
	ont_name = str(input("Please enter the ontology file name *.owl: "))

	#check if exists 
	full_path = ont_path + "\\" + ont_name
	
	if os.path.exists(full_path) == False:
		print("The given file doesn't exist")
	else:
		try:
			print("File found (500)")
			onto_path.append(ont_path)
			onto = get_ontology(ont_name)
			onto.load()
			#load Operations
			try:
				while cont == "y":
					choice = load_operations()
					handle_operations(choice, onto)
					cont = str(input("Do you want to continue ? y/n "))
				if cont == 'n':
					print("Thanks for using Ontology browser :)")
			except:
				print("unknown choice")
		except:
			print("Cannot load the Ontology")
