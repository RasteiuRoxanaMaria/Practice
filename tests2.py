import calculateSum

add = calculateSum.addV
diff = calculateSum.diffV
multiplication = calculateSum.multiplicationV
division = calculateSum.division

# 1st test
assert add == 19 , "1st TEST --> FAILED"
print("1st TEST --> PASSED")

# 2nd test
assert diff == 11 , "2nd TEST --> FAILED"
print("2nd TEST --> PASSED")

# 3rd test
assert multiplication == 76 , "3rd TEST --> FAILED"
print("3rd TEST --> PASSED")

# 4th test
assert division == 6, "4th TEST --> FAILED"
print("4th TEST --> PASSED")