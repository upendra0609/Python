user_list = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
position = int(input("Enter position :"))
col = position % 10
position = int(position / 10)
row = position % 10
user_list[row - 1][col - 1] = 'X'
print(user_list[0])
print(user_list[1])
print(user_list[2])
