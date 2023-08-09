class Circle:
    def __init__(self, r):
        self.radius = r
        self.p = 3.14
    def area(self):
        return (self.radius **   2) * self.p
    
    def perimeter(self):
        return (self.radius * 2) * self.p
    
class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)

    def area(self):
        return (self.radius ** 2) * (self.p * 4)
    
z = float(input("enter your number for circle: "))    
circle = Circle(z)
print("perimeter of circle:", circle.perimeter())
print("area of circle:", circle.area())

x = float(input("enter your number for sphere: "))
sphere = Sphere(x)
print("area of sphere:", sphere.area())