# Dakota Bourne db2nb
import urllib.request
word_lst = []
file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
for word in file:
    wordy = word.decode('utf-8').strip().lower()
    word_lst.append(wordy)
words = input('Type text; enter a blank line to end.\n')
while True:
    if words == '':
        break
    new_words = words.split(' ')
    for i in new_words:
        new_word = i.strip(".?!,()' '").strip('"').strip(" ' ").lower()
        if new_word != '':
            if new_word not in word_lst:
                print("  MISSPELLED", new_word)
    words = input('')
