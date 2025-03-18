class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"Item({self.name},{self.price})"
item1 = Item("Laptop",50000)
item2 = Item("Mouse",1000)
print(item1)
print(item2)
