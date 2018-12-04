# Dakota Bourne db2nb
"""
This program has a function designed to take in a single string, with one of the four major operators, and depending on
the operator, slices off the string before the operator and the string after, and completes the operation by using the
respective operator to calculate what the user intended.
"""


def binop(s):
    if "+" in s:
        f = s.find("+")
        g = len(s)
        h = int(s[0:f])
        i = int(s[f + 1:g])
        j = int(h + i)
        return j
    elif "-" in s:
        f = s.find("-")
        g = len(s)
        h = int(s[0:f])
        i = int(s[f + 1:g])
        j = int(h - i)
        return j
    elif "*" in s:
        f = s.find("*")
        g = len(s)
        h = int(s[0:f])
        i = int(s[f + 1:g])
        j = int(h * i)
        return j
    else:
        f = s.find("/")
        g = len(s)
        h = int(s[0:f])
        i = int(s[f + 1:g])
        j = float(h / i)
        return j
