import math

def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    area = math.pi * (radius * radius)
    return area
    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculate the area of a circle.")
    parser.add_argument('radius', type=float, help='The radius of the circle')

    args = parser.parse_args()
    
    area = circle_area(args.radius)
    print(f'The area of the circle with radius {args.radius} is: {area}')