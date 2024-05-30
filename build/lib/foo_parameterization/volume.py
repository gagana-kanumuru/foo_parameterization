import math

def calculate_volume(radius):
    """
    Calculate the volume of a sphere given its radius using the formula:
    Volume = 4/3 * π * r^3
    
    Parameters:
    radius (float): Radius of the sphere
    
    Returns:
    float: Volume of the sphere
    """
    if radius <= 0:
        raise ValueError("Radius must be positive")
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
