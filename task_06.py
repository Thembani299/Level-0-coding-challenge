def maximum(*arg_numbers):
    maxim=arg_numbers[0]
    for i in arg_numbers:
        if i>maxim:
            maxim=i
    return maxim
print(maximum(-2,-3,-1))


