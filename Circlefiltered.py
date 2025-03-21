class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __str__(self):
        return f"Circle({self.radius})"
    def get_area(self):
        self.area = 3.14*self.radius*self.radius
        return self.area
circles =[]
n = int(input("How many circles: "))
for i in range(n):
        r = float(input(f"Enter radius of circle{i+1}: "))
        circles.append(Circle(r))
filtered_circles = [i for i in circles if i.get_area()<100]
for i in filtered_circles:
    print(i)
