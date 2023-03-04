import sys

def sorted_fusion():
    i = 1
    array1 = []
    array2 = []
    new_array = []

    while i < len(sys.argv):
        if sys.argv[i].isdigit():
            array1.append(int(sys.argv[i]))
            i = i + 1

        elif isinstance(sys.argv[i], str):
            i = i + 1
            while i < len(sys.argv):
                if sys.argv[i].isdigit():
                    array2.append(int(sys.argv[i]))
                    i = i + 1
                else:
                    ("Error.")

    #array1.sort()
    #array2.sort()

    try:
        j = 0
        k = 0
        i = 0
        while j < len(array1) and k < len(array2):
            if array1[j] < array2[k]:
                new_array.append(array1[j])
                j = j + 1

            elif array2[k] < array1[j]:
                new_array.append(array2[k])
                k = k + 1

        if array1[-1] > array2[-1]:
            new_array.append(array1[-1])
        elif array1[-1] < array2[-1]:
            new_array.append(array2[-1])

        return new_array

    except IndexError():
        pass

resultat = sorted_fusion()

for element in resultat:
    print(element, end=" ")

