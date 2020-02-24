if __name__ == '__main__':
    N = int(input())
    input_list = []
    final_list = []
    for i in range(N):
        a = list(map(str, input().split()))
        input_list.append(a)
    
    for i in range(len(input_list)):
        if input_list[i][0] == 'insert':
            final_list.insert(int(input_list[i][1]), int(input_list[i][2]))
        elif input_list[i][0] == 'print':
            print(final_list)
        elif input_list[i][0] == 'remove':
            final_list.remove(int(input_list[i][1]))
        elif input_list[i][0] == 'append':
            final_list.append(int(input_list[i][1]))
        elif input_list[i][0] == 'sort':
            final_list.sort()
        elif input_list[i][0] == 'reverse':
            final_list.reverse()
        else:
            final_list.pop(len(final_list)-1)
            