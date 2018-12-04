# Dakota Bourne (db2nb)
"""
mymap is designed to take a single argument mathematical function and apply it to each number in a list, and putting
each new number into a new list which is returned.
myreduce is designed to take a double argument mathematical function and apply it to each number in a list over and over
again, until a single integer is resulted from the operations, which is returned.
"""


def mymap(func, lst):
    new_lst = []
    for i in lst:
        new_num = func(i)
        new_lst.append(new_num)
    return new_lst


def myreduce(func, lst):
    n = 0
    new_num = 0
    for i in lst:
        n += 1
        if n == 1:
            init_i = i
        elif n == 2:
            new_num = func(init_i, i)
        if n > 2:
            new_num = func(new_num, i)
    return new_num
