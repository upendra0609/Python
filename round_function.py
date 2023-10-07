# in case of xx.5 return nearest even integer
a = round(12.5, 0)
b = round(11.5, 0)
print(a, b)

# if we pass -ve number then it will affect integer also
# 10^(-no of digits)  i.e 10^(-(-1)) = 10 closest to 10 multiple number
a = round(123, -1)
print(a)
a = round(12.67, -1)
print(a)

