class rectangle:                                               #class make name rectangle 
    def __init__(self ,width,height):                          #__init__()
        self.width = width
        self.height = height

    def area(self):                                            #method for calc. area 
        return self.width * self.height
    
    def perimeter(self):                                       #method for calc. perimeter
        return 2 * (self.width + self.height)
    
    def display(self):                                         #method to display
        print(f"Width : {self.width} , Height : {self.height}")

width = float(input("Enter width : "))                         #user input for width
height = float(input("Enter height : "))                       #user input for height

#rect = rectangle(5,10)                                         #for already inputted value   /   object creation for class rectangle  ->  rect
rect = rectangle(width, height)                                #for user input value  /  object creation for class  rectangle ->  rect
print(f"Area : {rect.area()}")                                 #with object rect + area() method call
print(f"Perimeter : {rect.perimeter()}")                       #with object rect + perimeter() method call
rect.display()                                                 # display the width and height inputted 