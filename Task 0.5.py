from cmath import sqrt


def area_of_triangle(length1,length2,length3):
    semiperimeter=1/2*(length1+length2+length3)
    area=sqrt(semiperimeter*(semiperimeter-length1)*(semiperimeter-length2)*(semiperimeter-length3))
    return abs(area)
