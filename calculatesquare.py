class Square:
    def __init__(self,s):
        self.side = s
    def calculate(self):
        self.area = self.side*self.side
        print(self.area)
        self.peri = self.side*4
        print(self.peri)
s1 = Square(5)
s1.calculate()
s2 = Square(20)
s2.calculate()
