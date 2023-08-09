class Triangle:
    def __init__(self, h, b, s1, s2):
        self.h = h
        self.b = b
        self.s1 = s1
        self.s2 = s2

    def triangle_area(self):
        return (0.5 * self.b) * self.h

    def triangle_environment(self):
        return self.s1 + self.s2 + self.b
    
class Square:
    def __init__(self, z):
        self.z = z

    def square_area(self):
        return self.z * self.z

    def square_environment(self):
        return 4 * self.z

class Pyramid(Square):
    def __init__(self, t, e):
        super().__init__(t)
        self.t = t
        self.e = e
    
    def pyramid_volume(self):
        return self.e * self.square_area() * (self.t / 3)
    
    def pyramid_area(self):
        return ((self.square_environment() * self.e) / 2) + self.square_area()

pyramid = Pyramid(5, 6)
square = Square(7)
triangle = Triangle(8, 2, 3, 5)

print(f"pyramid area = {pyramid.pyramid_area()} peramid volumn = {pyramid.pyramid_volume()}\n triangle area = {triangle.triangle_area()} triangle environment = { triangle.triangle_environment()}\n square area = {square.square_area()} square environment = {square.square_environment()}")