#to create abstract class in python import ABC from abc module and to create an abstract method import abstractmethod from abc module
from abc import ABC,abstractmethod
class AbstractClass(ABC):
    def abstractmethod1(self1):
        print("This is an abstract method in abstract class. All Abstract methods must be used in child class")
    def abstractmethod2(self2):
        print("This is second abstract method of abstract clas.The object of this class cannot be created it is only used for inheritance")
class ChildClass(AbstractClass):
    def abstractmethod1(self3):
        print("Abstract method1 is overridden here")
    def abstractmethod2(self4):
        print("Abstract method2 is overridden here")
object=ChildClass()
object.abstractmethod1()
object.abstractmethod2()
#obj=AbstractClass() will generate error message of "Can't instantiate abstract class AbstractClass without an implementation for abstract method 'abstractmethod1'"