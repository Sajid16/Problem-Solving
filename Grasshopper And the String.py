a = list(input())
prev_result, curr_result, no_vowel = 0, 0, 0

vowel = ['A', 'E', 'I', 'O', 'U', 'Y']

if len(a) > 1:
    for char in a:
        curr_result += 1
        if char not in vowel:
            no_vowel = curr_result
        elif char in vowel and curr_result >= prev_result:
            prev_result = curr_result
            curr_result = 0

else:
    for char in a:
        curr_result += 1
        if char in vowel and curr_result >= prev_result:
            prev_result = curr_result
            curr_result = 0
        else:
            prev_result = curr_result+1

if no_vowel == len(a):
    print(no_vowel+1)
else:
    print(prev_result)

