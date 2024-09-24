def check_triangle_type():
    a = float(input("insert a: "))
    b = float(input("insert b: "))
    c = float(input("insert c: "))

    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Is Equilateral Triangle")
        elif a == b or b == c or a == c:
            print("Is Isosceles Triangle")
        else:
            print("Is Scalene Triangle")
    else:
        print("Not a triangle")


check_triangle_type()