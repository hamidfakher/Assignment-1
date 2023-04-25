def pascal(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle

def pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row))

n = int(input("please enter row number of pascal: "))

pascals_triangle2 = pascal(n)
pascals_triangle(pascals_triangle2)
