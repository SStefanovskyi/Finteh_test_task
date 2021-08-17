my_list = [8, 2, 3, 1, 5, 6, 2]
lesser = 3
my_list.sort()


def slice_less():
    for i in range(len(my_list)):
        if my_list[i] > lesser:
            print(my_list[i])


slice_less()