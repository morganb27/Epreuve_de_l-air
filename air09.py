import sys

def ma_rotation(array):
    i = 0
    new_array = []
    while i < (len(array)):
        new_array.append(array[i])
        i = i + 1
    first_elem = new_array.pop(0)
    new_array.append(first_elem)
    return new_array

resultat = ma_rotation(sys.argv[1:])
print(", ".join(map(str, resultat)))
