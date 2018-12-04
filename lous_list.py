# Dakota Bourne db2nb
"""
This program has two functions, instructors and class_search, both of which are called generally out side of the program
itself
"""
import urllib.request


def instructors(department):
    """instructors takes a department name and returns an akphabetically sorted list of the teachers in that department"""
    teacher = []
    file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + str(department))
    for line in file:
        lst = line.decode('utf-8').strip().split('|')
        name = lst[4]
        if '+' in name:
            teacher_name = name[0:len(name)-2]
        else:
            teacher_name = lst[4]
        if teacher_name not in teacher:
            teacher.append(teacher_name)
    teachernames = sorted(teacher)
    return teachernames


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    """class_search is a function that takes a department name, true or false for has_seats_available none or an integer for level
    none or integer for not_before and the same for not_after"""
    new_lst = []
    file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + str(dept_name))
    for line in file:
        lst = line.decode('utf-8').strip().split('|')
        if has_seats_available:
            if lst[15] < lst[16]:
                if level:
                    if int(str(level)[0]) == int(lst[1][0]):
                        if not_before:
                            if int(not_before) >= int(lst[12]):
                                if not_after:
                                    if int(lst[12]) <= int(not_after):
                                        new_lst.append(lst)
                                else:
                                    new_lst.append(lst)
                        else:
                            if int(not_before) >= int(lst[12]):
                                if not_after:
                                    if int(lst[12]) <= int(not_after):
                                        new_lst.append(lst)
                                else:
                                    new_lst.append(lst)
                else:
                    if not_before:
                        if int(not_before) >= int(lst[12]):
                            if not_after:
                                if int(lst[12]) <= int(not_after):
                                    new_lst.append(lst)
                            else:
                                new_lst.append(lst)
                    else:
                        if int(not_before) >= int(lst[12]):
                            if not_after:
                                if int(lst[12]) <= int(not_after):
                                    new_lst.append(lst)
                            else:
                                new_lst.append(lst)
        else:
            if level:
                if int(str(level)[0]) == int(lst[1][0]):
                    if not_before:
                        if int(not_before) >= int(lst[12]):
                            if not_after:
                                if int(lst[12]) <= int(not_after):
                                    new_lst.append(lst)
                            else:
                                new_lst.append(lst)
                    else:
                        if not_after:
                            if int(lst[12]) <= int(not_after):
                                new_lst.append(lst)
                        else:
                            new_lst.append(lst)
            else:
                if not_before:
                    if int(not_before) >= int(lst[12]):
                        if not_after:
                            if int(lst[12]) <= int(not_after):
                                new_lst.append(lst)
                        else:
                            new_lst.append(lst)
                else:
                    if not_after:
                        if int(lst[12]) <= int(not_after):
                            new_lst.append(lst)
                    else:
                        new_lst.append(lst)
    return new_lst