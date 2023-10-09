name1 = input("enter name: ")
name2 = input("enter name: ")
name = name1 + name2
name = name.lower()
num1 = 0
num1 += name.count('t')
num1 += name.count('r')
num1 += name.count('u')
num1 += name.count('e')

num2 = 0
num2 += name.count('l')
num2 += name.count('o')
num2 += name.count('v')
num2 += name.count('e')

num = num1 * 10 + num2

print(num)
