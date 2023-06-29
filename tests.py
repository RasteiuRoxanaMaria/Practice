import calculateSum
from colorama import Fore

add = calculateSum.addV
diff = calculateSum.diffV
multiplication = calculateSum.multiplicationV
division = calculateSum.divisionV

# 1st test
assert add == 18 , Fore.RED + "1st TEST --> FAILED"
print(Fore.GREEN + "1st TEST --> PASSED")

# 2nd test
assert diff == 12 , Fore.RED + "2nd TEST --> FAILED"
print(Fore.GREEN + "2nd TEST --> PASSED")

# 3rd test
assert multiplication == 45 , Fore.RED + "3rd TEST --> FAILED"
print(Fore.GREEN + "3rd TEST --> PASSED")

# 4th test
assert division == 5 , Fore.RED + "4th TEST --> FAILED"
print(Fore.GREEN + "4th TEST --> PASSED")
