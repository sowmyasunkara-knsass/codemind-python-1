class Student:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print(f"Name is: {self.name}")

s1 = Student("Sowmya")
# print(s1.name)
s1.print_name()
