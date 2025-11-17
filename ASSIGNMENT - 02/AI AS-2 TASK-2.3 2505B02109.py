import math

def calculate_area(shape, **kwargs):
    """
    Calculates the area of a specified shape.

    Args:
        shape (str): The name of the shape ('square', 'rectangle', 'circle').
        **kwargs: Keyword arguments for dimensions (e.g., side, length, width, radius).

    Returns:
        float: The calculated area, or None if the shape or required arguments are invalid.
    """
    shape = shape.lower()

    if shape == 'square':
        if 'side' in kwargs:
            side = kwargs['side']
            return side * side
        else:
            return "Error: Square requires 'side' argument."

    elif shape == 'rectangle':
        if 'length' in kwargs and 'width' in kwargs:
            length = kwargs['length']
            width = kwargs['width']
            return length * width
        else:
            return "Error: Rectangle requires 'length' and 'width' arguments."

    elif shape == 'circle':
        if 'radius' in kwargs:
            radius = kwargs['radius']
            return math.pi * radius**2
        else:
            return "Error: Circle requires 'radius' argument."

    else:
        return "Error: Invalid shape specified."

# Example Usage:
print(calculate_area('square', side=5))
print(calculate_area('rectangle', length=4, width=6))
print(calculate_area('circle', radius=3))
