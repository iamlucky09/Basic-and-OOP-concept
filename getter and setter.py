# getter and setter in python 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def names(self):
        return self.name
    
    @names.setter
    def names(self, value):
        if not isinstance(value,str):
            raise ValueError("Name must be a string")
        self.name=value

    
    @property
    def ages(self):
        return self.age
    
    @ages.setter
    def ages(self,value):
        if not isinstance(value,int):
            raise ValueError("Age must be a integer")
        self.ages=value
    
   
per=person(3,3)
print(per.names)
print(per.ages)
per.names="kundan"
print(per.names)
per.ages="ages" # yesma error rise huncha kinavane tya mathi ages ma integer matra accept garne vanera lekhya cha
print(per.ages) #so, if you try to give a string you can see error {"Age must be an integer"}