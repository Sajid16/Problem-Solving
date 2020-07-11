import math

a = list(map(int, input().split()))


result = math.ceil(a[0] / a[2]) * math.ceil(a[1] / a[2])
print(result)
