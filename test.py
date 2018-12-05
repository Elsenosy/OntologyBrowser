from owlready2 import *

#load ontology from local 
onto_path.append("E:\\iContent\\Dr.Osama\\")
#load ontology from cloud 
onto = get_ontology("university.owl").load()

#make new class 

#class Again(onto.Module):
#	namespace = onto
	
#make new Property

class Drug(Thing):
    pass
class Ingredient(Thing):
    pass
class has_for_ingredient(ObjectProperty):
    domain    = [Drug]
    range     = [Ingredient]
#classess 
classes = list(onto.classes())
print("------------- Classes -----------------")
for i in range(len(classes)):
	print("{}-Class: {}".format(i,classes[i]))

#individuals 
individuals = list(onto.individuals())
print("------------- Individuals -----------------")
for x in range(len(individuals)):
	print("{}-Individual: {}".format(x,individuals[x]))

#object_properties 
obj_properties = list(onto.object_properties())
print("------------- Object Properties -----------------")
for y in range(len(obj_properties)):
	print("{}- {}".format(y,obj_properties[y]))

#data_properties
data_properties = list(onto.data_properties())

print("------------- Data Properties -----------------")
for z in range(len(data_properties)):
	print("{}- {}".format(z,data_properties[z]))


#Properties
properties = list(onto.properties())

print("------------- Properties -----------------")
for a in range(len(properties)):
	print("{}- {}".format(a,properties[a]))
	
#Disjoints
disjoint = list(onto.disjoints())

print("------------- Disjoints -----------------")

for d in range(len(disjoint)):
	#print classes 
	print(disjoint[d])

print("-------------------------------------------------")
print(onto.Again.is_a)
print(onto.Module.subclasses())

#create individual 
my_ind = onto.Again("my_ind")
#print(list(my_ind.get_properties()))
for n in individuals:
	print(list(n.get_properties()), end="\n\n")
	
#make a new property  Again to csModule 

#class has_again(ObjectProperty):
	#domain = [onto.Again]
	#range = [onto.CsModule]
onto.save()
