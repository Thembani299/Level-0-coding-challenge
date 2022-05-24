def area_of_triangle(length1,length2,length3):
    semiperimeter=1/2*(length1+length2+length3)
    area=(semiperimeter*(semiperimeter-length1)*(semiperimeter-length2)*(semiperimeter-length3))**0.5
    return area
print('Enter the 1st length')
length_1st=int(input())
print('Enter the 2nd length')
length_2nd=int(input())
print('Enter the 3rd length')
length_3rd=int(input())
print(area_of_triangle(length_1st,length_2nd,length_3rd))
