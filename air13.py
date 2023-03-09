#!/usr/bin/env python3.10

import os
import subprocess
from colorama import init, Fore, Style

init()

def output_script(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, _ = proc.communicate()
    return stdout.decode()

def full_test(test_name, command, expected, nb1, nb2):
    global success_count, failure_count
    test_count = 2
    print(f"\t{test_name} ({test_count} tests):")
    for i in range(1, test_count + 1):
        output = output_script(command)
        result = f"{test_name} ({nb1}/{nb2}) - Test {i}: "

        if expected in output:
            print(f"\t\t\033[32m{result}success\033[0m")
            success_count += 1
        else:
            print(f"\t\t\033[31m{result}failure\033[0m")
            failure_count += 1

success_count = 0
failure_count = 0

tests = {
    "air00": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air00.py "Bonjour les gars"', "expected": "Bonjour\nles\ngars"},
    "air01": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air01.py "Crevette magique dans la mer des étoiles" "la"', "expected": "Crevette magique dans \n mer des étoiles"},
    "air02": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air02.py "Je" "teste" "des" "trucs" " "', "expected": "Je teste des trucs"},
    "air03": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air03.py 1 2 3 4 5 4 3 2 1', "expected": "5"},
    "air04": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air04.py "Hello milady, bien ou quoi ??"', "expected": "Helo milady, bien ou quoi ?"},
    "air05": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air05.py 1 2 3 4 5 +2', "expected": "3 4 5 6 7"},
    "air06": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air06.py “Michel” “Albert” “Thérèse” “Benoit” “t”', "expected": "Michel"},
    "air07": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air07.py 1 3 4 2', "expected": "1 2 3 4"},
    "air08": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air08.py 10 20 30 fusion 15 25 35', "expected": "10 15 20 25 30 35"},
    "air09": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air09.py Michel Albert Thérèse Benoit', "expected": "Albert, Thérèse, Benoit, Michel"},
    "air10": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air10.py "mon_fichier.txt"', "expected": "je danse le mia !"},
    "air11": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air11.py 0 5', "expected": "    0\n   000\n  00000\n 0000000\n000000000"},
    "air12": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air12.py 1 2 3 4 5 4 3 2 1', "expected": "5"},
    "air14": {"path": "/Users/morganballouk/Desktop/Air", "command": 'python air14.py', "expected": "J'ai terminé l'épreuve de l'air et c'était faisable !\np.s. : Les deux derniers exos étaient vraiment difficiles."},
}

for test_name, test_data in tests.items():
    test_file = os.path.join(test_data["path"], f"{test_name}.py")
    if not os.path.isfile(test_file):
        print(f"{test_file} not found")
        continue
    full_test(test_name, test_data["command"], test_data["expected"], 1, 2)

print(Fore.GREEN + f"\nTotal success: ({success_count}/{success_count + failure_count})" + Style.RESET_ALL)
print(Fore.RED + f"Total failure: ({failure_count}/{success_count + failure_count})" + Style.RESET_ALL)
