# abstraction vaneko pani interface jastai nai ho ,vanda pani tei ho tara difference chai 
# k vanda chai yeskko chai class ma method ma arko normal method ni create garna sakincha and with abstract method 
# those both combining features vayeko lai nai abstract class vanincha.

from abc import ABC, abstractmethod

class vechile(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def fuel(self):
        return "fuel is important"
    
class car(vechile):

    def drive(self):
        print("you can drive a car")

    def stop(self):
        print("you can stop a car")

class truck(vechile):

    def drive(self):
        print("you can drive a truck")

    def stop(self):
        print("you can stop a truck")

c=car()
print(c.drive())
print(c.stop())
t=truck()
print(t.drive())
print(t.stop())
print(t.fuel())
