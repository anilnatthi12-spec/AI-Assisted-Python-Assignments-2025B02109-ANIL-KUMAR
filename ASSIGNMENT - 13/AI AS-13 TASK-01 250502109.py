def rectangle_area(x, y):
    """Calculate area of a rectangle."""
    return x * y

def square_area(x, _=0):
    """Calculate area of a square."""
    return x * x

def circle_area(x, _=0):
    """Calculate area of a circle."""
    return 3.14 * x * x

# Dispatch table mapping shape names to their corresponding functions
area_functions = {
    "rectangle": rectangle_area,
    "square": square_area,
    "circle": circle_area
}

def calculate_area(shape, x, y=0):
    """
    Calculates area based on shape type using dispatch table.

    Parameters:
    shape (str): Type of shape ('rectangle', 'square', 'circle')
    x (float): Primary dimension (e.g., side or radius)
    y (float): Secondary dimension (e.g., height for rectangle)

    Returns:
    float: Calculated area
    """
    func = area_functions.get(shape.lower())
    if func:
        return func(x, y)
    else:
        raise ValueError(f"Unsupported shape: {shape}")

# Sample usage with user input
if __name__ == "__main__":
    try:
        shape = input("Enter shape (rectangle, square, circle): ").strip().lower()
        x = float(input("Enter first dimension (e.g., side or radius): "))
        y = 0
        if shape == "rectangle":
            y = float(input("Enter second dimension (e.g., height): "))

        area = calculate_area(shape, x, y)
        print(f"The area of the {shape} is: {area}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")