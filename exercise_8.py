print("what number?")
num = input()
number_range = int(num) + 1

for num in range(number_range):
    for i in range(num):
        print(num, end=" ")
    print("")