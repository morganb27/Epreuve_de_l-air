import sys

def concat(lst, separator):
    lst = []
    i = 1
    str = ""

    while i < len(sys.argv)-1:
        lst.append(sys.argv[i])
        i = i + 1
        print(lst)

    for element in lst:
        i = 0
        if i == 0:
            str = str + element + separator
            i = i + 1
        else:
            str = str + separator + element
            i = i + 1

    return str

my_lst = []
my_separator = sys.argv[-1]
print(concat(my_lst, my_separator))




