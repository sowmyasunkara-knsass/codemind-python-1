class Person:
    population = 0 # class Attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.population+=1
print(Person.population)
p1 = Person("Xyz",2)
p2 = Person("pqr",17) 
print(p2.population)
print(Person.population)
