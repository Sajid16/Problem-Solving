
arr = []
n = int(input())

for i in range(n):

    x = int(input())
    arr.append(x)

k = int(input())


def findNumber(arr, k):
    for i in arr:
        if i == k:
            return 1
        else:
            pass


result = findNumber(arr, k)
if result == 1:
    print("YES")
else:
    print("NO")



