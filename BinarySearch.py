def search(array, key):
    begin = 0
    end = len(array) - 1
    # print(end)
    while begin <= end:
        mid = int((begin + end) / 2)
        # print(mid)
        if array[mid] == key:
            # by default binary search returns lower bound index
            return mid
            # if i want to return upper bound index
            # begin = mid + 1
        elif array[mid] > key:
            end = mid - 1
        elif array[mid] < key:
            begin = mid + 1
    return begin


inputArray = list(map(int, input().split()))
inputArray = sorted(inputArray)
print('Enter the searching number: ', end='')
n = int(input())
result = search(inputArray, n)
print(result)
inputArray.insert(result, n)
print(inputArray)
