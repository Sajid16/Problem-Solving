# count = 0
# straight = True
# reverse = False
#
# while straight:
#     if count <= 9:
#         count += 1
#         print(count, end=' ')
#     else:
#         reverse = True
#     while reverse:
#         if count >= 2:
#             count -= 1
#             print(count, end=' ')
#         else:
#             straight = False


######################################

#using one loop only

count = 0
start = True
stop = False

while stop == False:
    if start == True:
        count += 1
        print(count, end=' ')
        if count >= 10:
            start = False
    elif start == False:
        count -= 1
        print(count, end=' ')
        if count == 1:
            stop = True
