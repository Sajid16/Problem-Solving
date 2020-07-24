range_number = int(input())
prime_list = []

for i in range(2, range_number + 1):
    temp = 0
    for j in range(2, int((i / 2)) + 1):
        if i % j == 0:
            temp = 1
    if temp == 0:
        prime_list.append(i)

print("the list of prime number within the range of 1 to {} is: {}".format(range_number, prime_list))
