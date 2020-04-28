l = int(input())
r = int(input())

def oddNumber(l, r):
    for i in range(l, r+1):
        if(i%2 != 0):
            print(i)
        else:
            pass


oddNumber(l, r)