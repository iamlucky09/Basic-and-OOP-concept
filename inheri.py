# inheritance in python
class animal:
    type="mammal"
    def __init__(self, name, legs):
        self.name=name
        self.legs=legs
    def bark(self):
        if self.name=="dog":
           print("Dogs barks as woof")

        else:
            print("This is not a dog")

dog=animal("dog",5)
print(dog.name)
print(dog.legs)
print(dog.bark())


