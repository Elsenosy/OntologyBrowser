
#print("Start Testing Area =======================")
	
#lista = ['taha', 'ahmed', 'ali']
#if 'taha' in lista:
#	print("yes it found")
#else:
#	print("No it doesn't found")
#print("End Testing =================================")

class Shape:
	name = "taha"
	def __init__(self):
		print("Class shape inherited")
	
class Door(Shape):
	def __init__(Shape):
		print(Shape.name)
		
	def setAuthor(self, name):
		self.name = name 
	
	def checkAttrExist(self, attr):
		attrbs = self.__dict__
		val = attrbs.get(attr)
		if val != "None" : 
			return True
		else:
			return False
	
	def getAuthor(self):
		if self.checkAttrExist("name") == True:
			return (self.name)
		else:
			return ""
	
door1 = Door()
door1.setAuthor("Taha")
print("Author name is:",door1.getAuthor())
