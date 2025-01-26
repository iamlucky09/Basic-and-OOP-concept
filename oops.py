# python ma object oriented programming
# classes 
class myclass: # this is a simple way to make a class 
    x=1
p1=myclass()
print(p1.x)

# lets alik different real world ma use hune wala class herau
class apple:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"

p1=apple("kundan",23)
print(p1)
print(p1.name,p1.age)
print(p1.age)


# yo chai arko function wala 

class name:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfun(self):
        print("My name is "+self.name)

    def myfun(abc):
        # print("I'm " + abc.age) # yesma chai abc.age lekhda integer bujena kya code le ani teslai str(abc.age) lekhna paryo ani bujcha ,string 
        print("I'm" + str(abc.age) )

p1.age=23

# del p1.age # yesle khasai impact chai parcha jasto chai lagena tara ni euta function delete garne 

p2=name("kundan",25)
p2.myfun()