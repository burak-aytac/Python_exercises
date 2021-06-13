def uns_array(*array):
    array = list(array)
    array.sort()
    print(array)
    new_list = []
    new_list1 = []
    toplam = int()
    for i in array:
        if i+1 in array or i-1 in array:
            new_list.append(i)
    for i in reversed(range(len(array)-1, max(new_list)+1)):
        new_list1.append(i)
        new_set = set(new_list).intersection(set(new_list1))
        new_set=list(new_set)
    print(new_set)
    return len(new_set)
print(uns_array(100, 4, 200, 105, 101, 1, 3, 104, 2, 102, 103))