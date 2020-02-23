if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = 0
    final_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                result = i+j+k
                if result != n:
                    list1 = []
                    list1.extend([i,j,k])
                    final_list.append(list1)
    print(final_list)