start_number = int(input())
end_number = int(input())

divisors = []
perfect_numbers = []
sum = 0

for i in range(start_number, end_number+1):
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            divisors.append(j)
    for div in divisors:
        sum += div
    if sum == i:
        perfect_numbers.append(i)
        divisors = []
        sum = 0
    else:
        sum = 0
        divisors = []

print(perfect_numbers)