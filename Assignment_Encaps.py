class Encapsulate:
    def __private(self):
        print("This is a private value in Encapsulate Class")
    def _protected(self):
        print("This is a protected value in Encapsulate Class")
    def public(self):
        print("This is a public value in Encapsulate Class")
        
        
class Derived(Encapsulate):
    def __private(self):
        print("This is a private value in Derived Class")
    def _protected(self):
        print("This is a protected value in Derived Class")
    def public(self):
        print("This is a public value in the Derived Class")



Encapsulate = Encapsulate()
Encapsulate.public()
Encapsulate._protected()
Encapsulate._Encapsulate__private()


derived = Derived()
derived.public()
derived._protected()
derived._Derived__private()
derived._Encapsulate__private()





class Protected:
    def __init__(self):
        self.__privateVar = 86

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(68)
obj.getPrivate()
