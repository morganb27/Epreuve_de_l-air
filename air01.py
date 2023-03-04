import sys

arg = sys.argv[1]

def split_string(s, pattern):
    word = ""
    lst = []
    i = 0
    while i < len(s)-1:
        char = s[i]
        next_char = s[i+1]
        if char + next_char == pattern:
            lst.append(word)
            word = ""
            i = i + 2
        else:
            word = word + char
            i = i + 1
    # Ajoutez le dernier mot à la liste
    word = word + s[-1]
    lst.append(word)
    i = 0
    while i < len(lst):
        print(lst[i])
        i = i + 1

split_string(arg, sys.argv[2])
