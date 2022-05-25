def area_of_triangle(length1,length2,length3):
    semiperimeter=1/2*(length1+length2+length3)
    area=(semiperimeter*(semiperimeter-length1)*(semiperimeter-length2)*(semiperimeter-length3))**0.5
    return area
print(area_of_triangle(5,6,7))
