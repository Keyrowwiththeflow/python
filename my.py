print("Hello world")
numbers_list = [int(n) for n in input("Input a list of numbers").split()]
count = 0
for x in numbers_list:
    if x == 0:
        count = count + 1
print(count)