# Polymorphism ,is a used in a class method, ja chai multiple class huncha tara method ko name chai same huncha
class name:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def space(self):
        print("I am a man")

class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def space(self):
        print("I am an animal")

class fish:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def space(self):
        print("I am a fish")

p1=name("kundan",22)
p2=animal("horse",50)
p3=fish("fish",10)

for x in (p1,p2,p3):
    x.space()