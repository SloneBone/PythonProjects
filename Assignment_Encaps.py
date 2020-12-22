#The underscore syntax used in this file ( leading '_' and '__' with no trailing underscores)
#invoke Python  technique called 'name mangling' to protect from clashes when inherited
"""
NOTE 1:
Class-private names. Names in this category, when used within the context
of a class definition, are re-written to use a mangledform to help avoid
name clashes between “private” attributes/methods of base and derived classes.

NOTE 2:
Private name mangling: When an identifier that textually occurs in a class definitionbegins with two or more
underscore charactersand does not end in two or more underscores,it is considered a private name of that class.
Private names are transformed to a longer form before code is generated for them. The transformation
inserts the class name, with leading underscores removed and a single underscore inserted, in front of the name.
For example, the identifier __spam occurring in a class named Ham will be transformed to _Ham__spam.
This transformation is independent of the syntactical context in which the identifier is used.

"""


#Setting up Parent Class with private, protected and public functions
class Encapsulate:
    def __private(self):
        print("This is a private value in Encapsulate Class")
    def _protected(self):
        print("This is a protected value in Encapsulate Class")
    def public(self):
        print("This is a public value in Encapsulate Class")

#Setting up a Subclass to the parent class with private, protected and public functions
#I did this to show the relation of the two classes using these functions
class Derived(Encapsulate):
    def __private(self):
        print("This is a private value in Derived Class")
    def _protected(self):
        print("This is a protected value in Derived Class")
    def public(self):
        print("This is a public value in the Derived Class")


#Creating an instance of the parent class 'Encapsulate'
Encapsulate = Encapsulate()
#Calling the  instance of public method in 'Encapsulate' class
Encapsulate.public()
#Using Python underscore syntax '_' to call the protected method in 'Encapsulate' class 
Encapsulate._protected()
#Using Python double underscore syntax '__' to call the private method in 'Encapsulate' class 
Encapsulate._Encapsulate__private()

#Creating an instance of the child class 'Derived'
derived = Derived()
#Calling the instance of public method in the 'Derived' subclass
derived.public()
#Using Python underscore syntax '_'  to call the protected method in 'Derived' subclass 
derived._protected()
#Using Python underscore syntax '_' and '__' to call the private method in subclass 'Derived'
derived._Derived__private()
#Using Python underscore syntax '_' and '__' to call the private method in parent class 'Encapsulate'
#I did this to show that you can reach a private method of a parent class through a subclass
derived._Encapsulate__private()




#Note: this  part below is for study purposes only
# I kept it on this page purely for convenience 
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
