class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        self.area = self.length*self.width
    def print_area(self):
        print(self.area)
r1 = Rectangle(2,3)
r1.calculate_area()
r1.print_area()
