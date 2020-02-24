input_list = []
addition, subject, average = 0.0, 0, 0.0
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        a = list(map(str, input().split()))
        input_list.extend([a])
    name = str(input())
    for x in range(len(input_list)):
        #print(input_list[x])
        if input_list[x][0] == name:
            #print(len(input_list[x]))
            for i in range(1,len(input_list[x])):
                addition = addition + float(input_list[x][i])
                subject += 1
            break

    average = addition/subject
    print("{:.2f}".format(average))
