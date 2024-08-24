class Encapsulation:
    def __init__(self,name="Najaf Ali",age=19):
        #in python by default everything is Public but to make variable private syntax is self.__variablename=variablename
        self.__name=name
        self.age=age
obj1=Encapsulation()
print(obj1.age)
#syntax to access a private variable in python is objname._classname__privatevariable. This technique is called Name mangling.
#Name mangling is the process of changing name of a member with double underscore to the form object._class__variable
print("Private variable is: ",obj1._Encapsulation__name)

#Note: Python doesn't implement encapsulation exactly as per the theory of object-oriented programming.