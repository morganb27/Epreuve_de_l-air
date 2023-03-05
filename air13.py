#!/usr/bin/env python3.10


import os
import subprocess
from colorama import init, Fore, Style

init()

tests = {
    "air00": {"path": "/Users/morganballouk/Desktop/Air", "count": 3},
    "air01": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air02": {"path": "/Users/morganballouk/Desktop/Air", "count": 1},
    "air03": {"path": "/Users/morganballouk/Desktop/Air", "count": 1},
    "air04": {"path": "/Users/morganballouk/Desktop/Air", "count": 3},
    "air05": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air06": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air07": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air08": {"path": "/Users/morganballouk/Desktop/Air", "count": 3},
    "air09": {"path": "/Users/morganballouk/Desktop/Air", "count": 1},
    "air10": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air11": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air12": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air13": {"path": "/Users/morganballouk/Desktop/Air", "count": 2},
    "air14": {"path": "/Users/morganballouk/Desktop/Air", "count": 3},
}

success_count = 0
failure_count = 0

for test_name, test_data in tests.items():
    test_count = test_data["count"]
    print(f"Testing {test_name} ({test_count} tests):")
    for i in range(1, test_count + 1):
        test_file = os.path.join(test_data["path"], f"{test_name}.py")

        if not os.path.isfile(test_file):
            print(f"\t{test_file} not found")
            continue
        try:
            output = subprocess.check_output(["python", test_file], stderr=subprocess.STDOUT, timeout=5)
        except subprocess.CalledProcessError as e:
            print(f"\tTest {i} failed: {e.output.decode('utf-8')}")
            failure_count += 1
        except subprocess.TimeoutExpired:
            print(f"\tTest {i} timed out")
            failure_count += 1
        else:
            print(f"\tTest {i} succeeded")
            success_count += 1

print(Fore.GREEN + f"\nTotal success: ({success_count}/{success_count + failure_count})" + Style.RESET_ALL)
print(Fore.RED + f"Total failure: ({failure_count}/{success_count + failure_count})" + Style.RESET_ALL)
