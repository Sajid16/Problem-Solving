# reverse of a sentence

# string = input()
#
# list1 = string.split()
# for i in range(len(list1)-1, -1, -1):
#     print(list1[i], end=' ')

####################################################################


# reverse of the words of a sentence

# string = input()
#
# list1 = string.split()
# list2, result = [], []
# for i in range(0, len(list1)):
#     list2 = list(list1[i])
#     for j in range(len(list2) - 1, -1, -1):
#         result.append(list2[j])
#     result.append(' ')
#     # print(list2, end=' ')
#
# for letters in result:
#     print(letters, end='')

#################################################

# for i in range(200, 0, -1):
#     if i % 3 == 0:
#         print(i, end=' ')


##############################################

numbers = list(map(int, input().split(',')))
result = []
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[j] == numbers[i] and numbers[j] not in result:
            result.append(numbers[i])
    # print(i)
print(result)

###########################################
#
# total = 0
# test2 = []
# result = ''
#
# with open('input.txt', 'r') as inp, open('output.txt', 'w') as outp:
#     for line in inp:
#         try:
#             # print(line)
#             test1 = list(line)
#             for i in range(len(test1) - 1, -1, -1):
#                 # if test1[i] == '\n':
#                 #     pass
#                 # else:
#                 test2.append(test1[i])
#             # num = int(line)
#             # total += num
#         except ValueError:
#             print('{} is not a number!'.format(line))
#     # outp.write(str(total))
# for words in test2:
#     if words != '\n':
#         result += words
#     else:
#         result += ' '
# print(result)
# # print('Total of all numbers: {}'.format(total))
#
# ####################################################
#
# total = 0
#
# with open('input.txt', 'r') as inp, open('output.txt', 'w') as outp:
#     for line in inp:
#         try:
#             num = float(line)
#             total += num
#             outp.write(line)
#         except ValueError:
#             print('{} is not a number!'.format(line))
#
# print('Total of all numbers: {}'.format(total))
