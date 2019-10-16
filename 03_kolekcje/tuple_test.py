my_tuple = ('a', 3.4, 77, 3j + 4)

tmp_list = list(my_tuple)
tmp_list.remove(77)
print(tmp_list)
my_tuple = tuple(tmp_list)

