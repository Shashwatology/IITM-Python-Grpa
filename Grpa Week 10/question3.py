class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None
        
    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')

class Square(Shape):
    def __init__(self, side):
        # (2) Call base constructor and set name to "Square"
        super().__init__("Square")
        # (3) Assign side to the attribute
        self.side = side
        # (4) Call the compute methods
        self.compute_area()
        self.compute_perimeter()
        
    def compute_area(self):
        # (5) Compute area and assign to self.area (inherited from Shape)
        self.area = self.side * self.side
        
    def compute_perimeter(self):
        # (6) Compute perimeter and assign to self.perimeter (inherited from Shape)
        self.perimeter = 4 * self.side
