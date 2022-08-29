class rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self,width=None,height=None):
        if not( width == None and height == None):
            return width * height
        else:
            self.area = self.width * self.height
            return self.area
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

def print_(x,end="\n"):
    print(x+end)