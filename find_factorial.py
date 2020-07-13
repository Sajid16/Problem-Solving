start_number = int(input())
end_number = int(input())


for i in range(start_number, end_number + 1):
    factorial = 1
    if i == 0 or i == 1:
        print("Factorial of {} is: 1".format(i))
    else:
        for j in range(2, i + 1):
            factorial = factorial * j
        print("Factorial of {} is: {}".format(i, factorial))
