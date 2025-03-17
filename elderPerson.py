class Person:
    population = 0 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.population+=1
def print_elder(p1,p2):
    if p1.age>p2.age:
        print("Person1 is elder to person2")
    else:
        print("person2 is elder to person1")
print_elder(Person("xyz",2),Person("pqr",17))
