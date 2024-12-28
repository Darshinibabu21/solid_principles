class shape:
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

def print_area(shape):
    print("area :",shape.area())

rect=rectangle(4,5)
print_area(rect)

sq=square(6)
print_area(sq)
