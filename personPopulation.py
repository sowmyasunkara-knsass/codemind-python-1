class Person:
    population = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.population+=1
persons = []
for i in range(5):
    n = input("Enter your name: ")
    a = int(input("Enter your age: "))
    persons.append(Person(n,a))
for person in persons:
    print(person.name)
