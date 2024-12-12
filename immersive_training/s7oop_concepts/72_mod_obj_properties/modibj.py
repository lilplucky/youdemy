""""""
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def FirstFunc(self):
        print("Hi my name is " +self.name)

obj1 = person("Terry",36)

obj1.age = 50
obj1.name = "Emilio"

print(obj1.name)
print(obj1.age)
