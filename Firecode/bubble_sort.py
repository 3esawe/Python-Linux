def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(1,len(a_list)-i):
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
    return a_list
bubble_sort([1,2,0])
