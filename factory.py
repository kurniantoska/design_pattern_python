class ShapeInterface():
    def __init__(self):
        print('going factory interface')
        
        
class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")
        
        
class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")
        

class ShapeFactory():
    @staticmethod
    def getShape(type):
        if type == "circle" :
            return Circle()
        if type == "square":
            return Square()
        assert 0, 'Could not find shape' + type    
        
