#composition 
#how composition is done vanda ,composition is done by following

class A: #component ho yo
    def __init__(self):
        print("Component class is created")

    def m1(self):
        print("component method is created")

class B: # composite ho yo
    
    def __init__(self):

        self.obj1 = A()
        print("Composite class is created")

    def m2(self):
        
        self.obj1.m1()


obj2=B()
obj2.m2()
