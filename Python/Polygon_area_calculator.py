import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Sets the width of the rectangle.
    def set_width(self, width: float) -> None:
        self.width = width
    
    # Sets the height of the rectangle.
    def set_height(self, height: float) -> None:
        self.height = height
    
    # Returns area (width×height).
    def get_area(self) -> float:
        return self.width*self.height

    # Returns perimeter 2(width+height)
    def get_perimeter(self) -> float:
        return 2*(self.width+self.height)

    # Returns diagonal sqr(width² + height²)
    def get_diagonal(self) -> float:
        return math.sqrt(self.width**2 + self.height**2)

    # Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: Too big for picture..
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture." 
        
        return(("*" * self.width + "\n") * self.height)

    # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            return (self.width // shape.width) * (self.height // shape.height)
        if isinstance(shape, Square):
            return (self.width // shape.side) * (self.height // shape.side)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
    
    def set_width(self, side: float) -> None:
        super().set_width(side)
        super().set_height(side) 

    def set_height(self, side: float) -> None:
        
        super().set_width(side)
        super().set_height(side) 

    def set_side(self, side):
        
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
