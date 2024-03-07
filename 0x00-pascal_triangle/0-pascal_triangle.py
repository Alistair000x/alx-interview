#!/usr/bin/python3
def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i-1]
        for j in range(1, i):
            row.append(last_row[j-1] + last_row[j])
        row.append(1)
        triangle.append(row)
    return triangle

print("\n".join(",".join(["[{}]".format(x) for x in row]) for row in pascal_triangle(5)))
