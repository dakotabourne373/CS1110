# Dakota Bourne (db2nb)
"""

"""


def check(cc):
    new_n = 0
    d = 0
    p = 0
    new_numb = 0
    new_num = 0
    cc_num = str(cc)
    cc_num_even = cc_num[1::2]
    cc_num_odd = cc_num[::2]
    if len(str(cc)) % 2 == 0:
        for i in cc_num_even:
            new_n += int(i)
        for i in cc_num_odd:
            d = int(i)
            d *= 2
            if d >= 10:
                for i in str(d):
                    p += 1
                    if p == 1:
                        new_num = int(i)
                    else:
                        new_numb = int(i) + new_num
                    if p == len(str(d)):
                        new_num = 0
            d += new_numb
    else:
        for i in cc_num_odd:
            new_n += int(i)
        for i in cc_num_even:
            d = int(i)
            d *= 2
            if d >= 10:
                for i in str(d):
                    p += 1
                    if p == 1:
                        new_num = int(i)
                    else:
                        new_numb = int(i) + new_num
                    if p == len(str(d)):
                        new_num = 0
            d += new_numb
    if (new_n + d) % 10 != 0:
        return False
    else:
        return True
