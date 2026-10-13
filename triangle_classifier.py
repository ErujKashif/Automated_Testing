def classify_triangle(a, b, c):
    # All sides must be positive and within the allowed range
    if a < 1 or b < 1 or c < 1:
        return "Invalid"

    if a > 200 or b > 200 or c > 200:
        return "Invalid"

    # Triangle inequality: sum of any two sides
    # must be greater than the third side
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    # Classify the triangle
    if a == b == c:
        return "Equilateral"

    elif a == b or a == c or b == c:
        return "Isosceles"

    else:
        return "Scalene"