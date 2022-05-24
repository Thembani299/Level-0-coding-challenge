def maximum(*argnumbers):
    maxim=argnumbers[0]
    for i in argnumbers:
        if i>maxim:
            maxim=i
    return maxim
print(maximum(-2,-3,-1))


