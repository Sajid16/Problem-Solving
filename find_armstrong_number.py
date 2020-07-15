start_number = int(input())
end_number = int(input())

result_list = []

for i in range(start_number, end_number + 1):
    sum = 0
    l = len(str(i))
    for j in list(str(i)):
        sum += int(j) ** l
    # print(sum)
    if sum == i:
        result_list.append(str(i))
# print(result_list)
print("The list of Armstrong number is: {}".format(result_list))
