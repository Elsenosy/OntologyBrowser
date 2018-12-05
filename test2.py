from owlready2 import *

onto_path.append("E:\iContent\Dr.Osama")
onto = get_ontology("new_ont.owl")

onto.load()

with onto:
    class Student(Thing):
        pass
    class Teacher(Thing):
        pass
    class teaches(ObjectProperty):
        domain = [Teacher]
        range = [Student]
    class has_name(DataProperty):
        domain = [Teacher, Student]
        range = [str]
    class has_id(DataProperty):
        domain = [Teacher, Student]
        range = [int]
    class has_title(DataProperty):
        domain = [Teacher]
        range = [str]
    class has_class(DataProperty):
        domain = [Student]
        range = [int]
    class has_registered(DataProperty):
        domain = [Student]
        range = [bool]

    student1 = Student("student1")
    student1.has_id.append(1)
    student1.has_name.append("Taha")
    teacher1 = Teacher("teacher1")
    teacher1.has_id.append(1)
    teacher1.has_name.append("David")
#save the module
onto.save()
print("""=======================================
    Classes:           {}
    Object properties: {}
    Data Properties:   {}
    Individuals:       {}
    A value:           {}
    """.format(list(onto.classes()), list(onto.object_properties()), list(onto.data_properties()), list(onto.individuals()), student1.has_name))