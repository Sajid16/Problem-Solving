string = list(map(str, input().split()))
# print(string)
count = 0
store = []
result = ''

for word in string:
    count += 1
    store.append(word + ' ')
    if count == 14:
        store.append('\n')
        count = 0
        # break

# print(store)
for word in store:
    result += word

print(result)