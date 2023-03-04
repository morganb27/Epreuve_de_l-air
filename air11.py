import sys

def escalier(caractere, n):
    for i in range(1, n+1):
        print(" "*(n-i) + caractere*(2*i-1))

escalier(sys.argv[1], int(sys.argv[2]))