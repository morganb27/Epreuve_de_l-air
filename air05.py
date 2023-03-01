import sys

def operation_sur_chaque_entier():
    i = 1
    try:
        while i < len(sys.argv) - 1:
            sys.argv[i] = int(sys.argv[i]) + int(sys.argv[-1])
            print(sys.argv[i], end = " ")
            i = i + 1

    except IndexError:
        pass

    except:
        print("Error.")


operation_sur_chaque_entier()

