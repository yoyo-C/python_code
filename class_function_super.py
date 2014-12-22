class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name = name
class Cat(Animal):
    def __init__(self,name):
        self.name = name

class  Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __int__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    def __int__(self, name):
        self.name = name

class Salmon(Fish):
    def test(self,name):
        print self.name

class Halibut(Fish):
    pass
        
rover = Dog('Rover')
print rover
satan = Dog('Satan')
print satan
mary = Person('Mary')
mary.pet = satan
frank = Employee(120000)

frank.pet = rover
print frank.pet

flipper = Fish('salmon')
crouse = Salmon()
harry = Halibut()