import sys

input_set = input("enter number separated with space")
string_set = input_set.split(" ")
num_set = set()
for num in string_set:
    num_set.add(int(num))

max_num = -sys.maxsize - 1

for i in num_set:
    if max_num < i:
        max_num = i

print(max_num)
