import sys

arg = sys.argv[1]
lst = []


def split_string(str, pattern):
    word = ""
    for char in str:
        if char in pattern:
            if len(word)>0:
                lst.append(word)
            word = ""

        else:
            word = word + char

    if len(word)>0:
        lst.append(word)


split_string(arg, [" ", "\t", "\n"])

i = 0
while i < len(lst):
    print(lst[i])
    i = i+1




