class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

'''class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length'''

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length, length)

class Cube(Square):
    def surfaceArea(self):
        faceArea = super().area()
        return faceArea * 6
    def Volume(self):
        faceArea = super().area()
        return self.length*faceArea

abcd = Cube(5)
print(abcd.Volume())

