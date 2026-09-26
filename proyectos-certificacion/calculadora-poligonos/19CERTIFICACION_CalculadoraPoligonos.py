import math

class Rectangle:
    def __init__(self,width: int, height: int):
        self.width = width
        self.height = height
        
    def set_width (self,width):
        self.width = width

    def set_height (self,height):    
     self.height = height
     
    def get_area(self) -> int:
        area = (self.height * self.width)
        return area
    
    def get_perimeter(self) -> int:
        perimetro = 2 * (self.width + self.height)
        return perimetro
    
    def get_diagonal(self) -> float:
        diagonal = (self.height ** 2 + self.width ** 2)
        diagonal_final = math.sqrt(diagonal)
        return diagonal_final
    
    def __str__(self) -> str:   
     return f"Rectangle(width={self.width}, height={self.height})"
 
    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:  
            return "Too big for picture."
         
        picture = ""
        for i in range (self.height):
         picture += ("*" * self.width) + "\n"  
        return picture
       
    def get_amount_inside(self,figura: str):
    
        figura_widht = self.width // figura.width
        figura_height = self.height // figura.height    
        
        return figura_widht * figura_height
    
class Square(Rectangle):
    def __init__(self,side: int):
        super().__init__(side,side)
        
    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side
       
    def set_side(self,side):
            self.set_width(side)
       
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
       
       
    