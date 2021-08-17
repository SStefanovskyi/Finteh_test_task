def slice_less(my_list, lesser):
    my_list.sort(reverse=True)
    for i in range(len(my_list)):
        if my_list[i] > lesser:
            print(my_list[i])