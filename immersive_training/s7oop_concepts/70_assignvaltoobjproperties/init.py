"""
All classes have a function called init
always exec when class is being initiated
"""
class person:
    def __init__(self,name,age):#self access variables that belong to this class
        self.name = name
        self.age = age

obj1 = person("Terry", 40)
print(obj1.name)
print(obj1.age)


