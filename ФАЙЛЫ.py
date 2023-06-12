nums = []


for i in range(4):
    b = input()
    nums.append(b +'\n')


with open('name.txt', 'a') as file:
    for i in nums:
        file.write(i)

with open('name.txt', 'r') as file:
    for i in file:
        print(i, end='')