def maximum_Func(num1,num2,num3):
    maximum = num1
    if num2>num1 and num2>num3:
        maximum = num2
    else:
        maximum = num3
    return maximum
val = maximum_Func(232,456,23)
print(val)