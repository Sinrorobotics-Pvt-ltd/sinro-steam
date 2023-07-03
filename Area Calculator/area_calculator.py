def calculate_area(shape):
    shape = shape.lower()
    
    if shape == "square":
        side_length = float(input("Enter the side length of the square: "))
        area = side_length ** 2
        return area
    
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        return area
    
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * (radius ** 2)
        return area
    
    elif shape == "triangle":
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        return area
    
    else:
        print("Invalid shape entered.")
        return None

# Example usage
shape_type = input("Enter the shape type (square, rectangle, circle, triangle): ")
result = calculate_area(shape_type)
if result is not None:
    print("The area is:", result)
