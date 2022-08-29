import new_factorial

result_1 = new_factorial.factorial(5)
assert result_1 == 120
result_1 = new_factorial.factorial(0)
assert result_1 == 1
result_1 = new_factorial.factorial(1)
assert result_1 == 1


result_1 = new_factorial.recursive_factorial(5)
assert result_1 == 120
result_1 = new_factorial.recursive_factorial(0)
assert result_1 == 1
result_1 = new_factorial.recursive_factorial(1)
assert result_1 == 1