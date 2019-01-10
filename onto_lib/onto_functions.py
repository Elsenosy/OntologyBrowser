from owlready2 import *


# =================================== Operation Functions ===============================================
# @return list of classes
def list_classes(onto):
    print("======================== List ontology Classes ==============================")
    count = 0
    cls = list()
    print("\n===== {} Classes ====".format(onto.name))
    if len(list(onto.classes())) != 0:
        for n in onto.classes():
            print(n)
            cls.append(n)
            count += 1
    print("Total: {}".format(count))
    return cls


# @return list of object properties
def list_rels(onto):
    print("======================== List ontology Relations ==============================")
    count = 0
    print("\n===== {} Relations ====".format(onto.name))
    if len(list(onto.object_properties())) != 0:
        for n in onto.properties():
            print(n)
            count += 1
    print("Total: {}".format(count))
    return list(onto.object_properties())


# @return list of object individuals
def list_indv(onto):
    print("======================== List ontology individuals ==============================")
    count = 0
    print("\n===== {} Individuals ====".format(onto.name))
    if len(list(onto.individuals())) != 0:
        for n in onto.individuals():
            print(n)
            count += 1
    print("Total: {}".format(count))
    return list(onto.individuals())


# @return list of data properties
def list_data_properties(onto):
    print("======================== List ontology data properties ==============================")
    count = 0
    for n in onto.data_properties():
        print(n)
        count += 1
    print("Total: {}".format(count))
    return list(onto.data_properties())


# get ontology Classes as only names, not with namespace.classname for ex: university.class = 'class'
def get_onto_class_names(onto):
    classNames = list()
    # append parent class (Thing)
    classNames.append("Thing")
    for className in onto.classes():
        NewClassName = str(className).split(".")[1]
        classNames.append(NewClassName)
    return classNames


def get_class_instances(onto, ontoClass):
    class_instances = list()
    called_class = onto[ontoClass]

    for instance in called_class.instances():
        instance_name = str(instance).split(".")[1]
        class_instances.append(instance_name)

    return class_instances

def insert_indv(onto):
    print("======================== Insert new Individual ==============================")
    try:
        onto_classes = get_onto_class_names(onto)
        print("Select a class to insert individual to it: ")
        i = 1
        for cls in onto_classes:
            print("{}. {}".format(i, cls))
            i += 1
        chosen_class = int(input("Chosen class: ")) - 1  # cuz it's a list
    except:
        print("Cannot load classes")
    try:
        #Call the Class
        calledClass = onto[onto_classes[chosen_class]]
        print("================== Class: {} individuals =================".format(onto_classes[chosen_class]))
        ind_name = str(input("Please enter the individual name: ")).replace(" ","")
        try:
            new_ind = calledClass(ind_name)
            onto.save()
            print("'{}' has been added succesfully".format(ind_name))
        except:
            print("Cannot add individual '{}'".format(ind_name))
    except:
        print("Cannot load the selected class")

def remove_individuals(onto):
    print("===================== Deleting Individual ==========================")
    try:
        onto_classes = get_onto_class_names(onto)
        print("Select a class to list it's individuals: ")
        i = 1
        for cls in onto_classes:
            print("{}. {}".format(i, cls))
            i += 1
        chosen_class = int(input("Chosen class: ")) - 1  # cuz it's a list
    except:
        print("Cannot load classes")
    try:
        called_class = onto_classes[chosen_class]
        class_instances = get_class_instances(onto, called_class)
        i = 1
        # loop through individuals
        for ind in class_instances:
            print("{}. {}".format(i, ind))
            i += 1
        chosen_instance = int(input("Chosen individual: ")) - 1
        try:
            onto_individual = onto[class_instances[chosen_instance]]
            destroy_entity(onto_individual)
            print("{} deleted successfully".format(onto_individual))
            onto.save()
        except:
            print("Cannot delete indvidual")
    except:
        print("Cannot get individuals")
    return True


# insert new Class
def insert_class(onto):
    print("======================== Insert new class ==============================")
    with onto:
        # Get all Classes
        list_of_classes = get_onto_class_names(onto)
        # Print all classes to choose class
        for i in range(0, len(list_of_classes)):
            print("{}. {}".format(i + 1, list_of_classes[i]))
        # Get the parent class
        classIndexChosen = int(input("Please select parent class: "))
        classIndexChosen -= 1
        # Load parent class as Ontology Entity
        calledClass = onto[list_of_classes[classIndexChosen]]
        # check if the parent class is Thing
        if (classIndexChosen == list_of_classes.index("Thing")):
            calledClass = Thing
        # Ask user for new class name, and trim spaces from that name
        NewClassName = str(input("Please enter class name: ")).replace(" ", "")

        # Check if class is not exists
        if NewClassName in get_onto_class_names(onto):
            print("Sorry, Class already exists")
        else:
            # create the new class and append it to the parent class
            NewClass = types.new_class(NewClassName, (calledClass,))
            # save Ontology
            onto.save()
            # check if it is saved
            if NewClassName in get_onto_class_names(onto):
                print("Class: '{}' which parent of '{}' has been added successfully".format(NewClassName,
                                                                                            list_of_classes[
                                                                                                classIndexChosen]))
def remove_class(onto):
    print("===================== Deleting Class ==========================")
    onto_classes = get_onto_class_names(onto)
    # Delete an class
    print("Choose a class to delete: ")
    i = 1
    for cls in onto_classes:
        print("{}. {}".format(i, cls))
        i += 1
    class_chosen = int(input("Class chosen: ")) - 1
    class_as_entity = onto[onto_classes[class_chosen]]
    try:
        destroy_entity(class_as_entity)
        print("Class '{}' deleted successfully".format(class_as_entity))
        onto.save()
    except:
        print("Cannot delete '{}'".format(class_as_entity))

def delete_onto_entity(onto):
    print("======================== Delete ontology concept ==============================")
    # First choose an item cat
    print("""
    Please select category:
        1. Class
        2. Individual
    """)
    cat = int(input("Category Chosen: "))
    # Switch category
    if cat == 1:
        remove_class(onto)
    elif cat == 2:
        remove_individuals(onto)
