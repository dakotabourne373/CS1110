# Dakota Bourne (db2nb)
"""
myfind is designed to take a word and a character and find the specific number that the character or character set is in
the word.
mysplit is designed to take a string and split the string up into a list based on the white spaces.
"""


def myfind(word, char):
    i = 0
    if len(char) == 1:
        while i < len(word):
            letter = word[i]
            if letter == char:
                return i
            i += 1
    if char not in word:
        return -1
    else:
        while char in word:
            newword = word[-i + 1:]
            i += 1
            if char not in newword:
                return i


def mysplit(word):
    new_l = []
    new_w = ''
    for i in word:
        if i == ' ':
            new_l.append(new_w)
            new_w = ''
        else:
            new_w += i
    if new_w:
        new_l.append(new_w)
    return new_l
