def check_point_belongs_rect(a, b, c):
    return a[0] <= c[0] <= b[0] and a[1] <= c[1] <= b[1]

print(check_point_belongs_rect((2,3),(6, 6), (3,4)))

