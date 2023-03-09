import sys

def insertion_dans_un_tableau_trie(lst, new_element):
    i = 0
    while i < len(lst):
        if int(new_element) < int(lst[i]):
            i = i + 1
        elif i == len(lst) - 1:
            lst.append(new_element)
            break
        elif int(new_element) > int(lst[i]) and int(new_element) < int(lst[i + 1]):
            lst.insert(i + 1, new_element)
            break
        else:
            i = i + 1


    return lst

result = insertion_dans_un_tableau_trie(sys.argv[1:-1], sys.argv[-1])
print(" ".join(result))