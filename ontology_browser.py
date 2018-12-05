from owlready2 import *
import os


cont = "y" #breaking var

#define script operations
def load_operations():
	operation = int(input("""
Please select an operation:
	1) List classes
	2) List object properties
	3) List individuals
	4) List data properties
	
	>> """))
	return operation

#Switch script operations
def handle_operations(option, onto):
	#switch an option
	option = int(option)
	if option == 1:
		#list all ontologu classes
		list_classes(onto)
	elif option == 2:
		#list all object properties
		list_rels(onto)
	elif option == 3:
		#list all individuals
		list_indv(onto)
	elif option == 4:
		#list all data properties
		list_data_properties(onto)
	else:
		print("Unkown operation")

# =================================== Operation Functions ===============================================
#@return list of classes
def list_classes(onto):
	count = 0
	cls = list()
	print("\n===== {} Classes ====".format(onto.name))
	if len(list(onto.classes())) != 0:
		for n in onto.classes():
			print(n)
			cls.append(n)
			count +=1
	print("Total: {}".format(count))
	return cls

#@return list of object properties
def list_rels(onto):
	count = 0
	print("\n===== {} Relations ====".format(onto.name))
	if len(list(onto.object_properties())) != 0:
		for n in onto.properties():
			print(n)	
			count +=1
	print("Total: {}".format(count))
	return list(onto.object_properties())

# @return list of object individuals
def list_indv(onto):
	count = 0
	print("\n===== {} Individuals ====".format(onto.name))
	if len(list(onto.individuals())) != 0:
		for n in onto.individuals():
			print(n)	
			count +=1
	print("Total: {}".format(count))
	return list(onto.individuals())

#@return list of data properties
def list_data_properties(onto):
	with onto:
		class Student(Thing):
			pass
		class std_name(DataProperty):
			domain = [Student]
			renge = [str]
		new_std = Student("new_std")
		new_std.std_name = "Taha"
	count = 0
	for n in onto.data_properties():
		print(n)
		count += 1
	print("Total: {}".format(count))
	return list(onto.data_properties())

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
