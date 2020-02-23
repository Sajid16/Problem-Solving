final_list = []
number_list = []
name_list = []

if __name__ == '__main__':
    for _ in range(int(input())):
        list1 = []
        name = input()
        score = float(input())
        ############# making 1st list of name and score ###############
        list1.extend([name,score])

        ############# integrate list1 to final_list ###############
        final_list.append(list1)

    ############# seperating numbers from final list and taking them into number_list ###############

    for i in range(len(final_list)):
        number_list.append(final_list[i][1])

    ############# sorting number_list and take the min value into min_num ###############

    number_list = sorted(number_list)
    min_num = min(number_list)

    ############# finding out the second minimum number from number_list comparing to min_num value
    # and if found then break loop
    # ###############

    for num in number_list:
        if num > min_num:
            second_min = num
            break
    #print(second_min)

    ############# comparing final_list numbers with second_min
    # if match then catch the name and append to name_list ###############

    for i in range(len(final_list)):
        if final_list[i][1] == second_min:
            #print(final_list[i][0])
            name_list.append(final_list[i][0])

    ############# sort the name_list and print the name ###############

    for name in sorted(name_list):
        print(name)