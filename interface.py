# interface and how its works
# in interface we need to implement using abstract base class(abc)
# for example
# and in interface all the method are abstract,no any normal method
# if there is a normal method too it is called as abstract class
from abc import ABC, abstractmethod # yo abc module implement garna parcha,abc->abstract base class

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height
    
c=square(2,3)
print(c.area())
