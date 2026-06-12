class shape:
    
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
class circle(shape):

    def __init__(self, color, is_filled, radius,width):
        super().__init__(color, is_filled)
        self.radius = radius
        self.width = width

class triangle(shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

Circle = circle(color="pink", is_filled=True, radius=5, width=3)
Triangle = triangle(color="red", is_filled="False", width="3") 

print(Circle.color)
print(Triangle.width)