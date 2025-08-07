def calculate_quandrant(x,y):
    # with zero(s)
    if x == 0 and y == 0:
        return "is the origin point!"
    elif x == 0:
        return "lying on Y-axis!"
    elif y == 0:
        return "lying on X-axis!"
    # without any zeros
    if x > 0 and y > 0:
        return "in Quadrant I"
    elif x < 0 and y > 0:
        return "in Quadrant II"
    elif x < 0 and y < 0:
        return "in Quadrant III"
    elif x > 0 and y < 0:
        return "in Quadrant IV"

def main():
    x_coordinate = int(input("X-Coordinate: "))
    y_coordinate = int(input("Y-Coordinate: "))
    print(f"({x_coordinate},{y_coordinate}) is {calculate_quandrant(x_coordinate,y_coordinate)}")

main()