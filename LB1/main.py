
def validate_radius(r):
    if r < 0:
        return False
    else: 
        return True

def get_circle_length(r):
    length = r * 2 * 3.14
    return length

def get_circle_area(r):
    area = pow(r, 2) * 3.14
    return area


if __name__ == "__main__":
    
    radius = int(input("Введіть радіус "))
    
    if validate_radius(radius):
        print("S = ", get_circle_area(radius))
        print("l = ", get_circle_length(radius))
    else:
        print("Радіус кола не може бути менше 0")