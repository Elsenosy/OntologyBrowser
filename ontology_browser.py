from owlready2 import *
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
	elif option == 5:
		#Insert new class
		insert_class(onto)
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

#get ontology Classes as only names, not with namespace.classname for ex: university.class = 'class'
def get_onto_class_names(onto):
	classNames = list()
	# append parent class (Thing)
	classNames.append("Thing")
	for className in list_classes(onto):
		NewClassName = str(className).split(".")[1]
		classNames.append(NewClassName)

	return classNames

# insert new Class
def insert_class(onto):
	with onto:
		# Get all Classes
		list_of_classes = get_onto_class_names(onto)
		# Print all classes to choose class
		for i in range(0, len(list_of_classes)):
			print("{}. {}".format(i+1, list_of_classes[i]))
		# Get the parent class
		classIndexChosen = int(input("Please select parent class: "))
		classIndexChosen -= 1
		# Load parent class as Ontology Entity
		calledClass = onto[list_of_classes[classIndexChosen]]
		#check if the parent class is Thing
		if(classIndexChosen == list_of_classes.index("Thing")):
			calledClass = Thing
		# Ask user for new class name, and trim spaces from that name
		NewClassName = str(input("Please enter class name: ")).replace(" ", "")

		#Check if class is not exists
		if NewClassName in get_onto_class_names(onto):
			print("Sorry, Class already exists")
		else:
			#create the new class and append it to the parent class
			NewClass = types.new_class(NewClassName, (calledClass,))
			#save Ontology
			onto.save()
			#check if it is saved
			if NewClassName in get_onto_class_names(onto):
				print("Class: '{}' which parent of '{}' has been added successfully".format(NewClassName, list_of_classes[classIndexChosen]))

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
