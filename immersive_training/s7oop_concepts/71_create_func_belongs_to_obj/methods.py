""""""
#creating a greeting function and execute it on the object
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def FirstFunc(self):
        print("Hi my name is " +self.name)
    
    def SecondFunc(self):
        print("Hi my age is " +str(self.age))

obj1 = person("Terry", 40)
obj1.FirstFunc()
obj1.SecondFunc()
