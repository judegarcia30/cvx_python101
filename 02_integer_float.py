# Integers are whole numbers
# Floats are decimal numbers

num = 3
num_float = 3.14
print(type(num))
print(type(num_float))

# Arithmetic Operators
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

num_1 = '100'
num_2 = '200'
print(num_1 + num_2)
print(int(num_1) + int(num_2))

# Order of operation by adding parenthesis
print(3 * 2 + 1) # result is 7
print(3 * ( 2 + 1 )) # result is 9

# incrementing a variable
num = 1
num = num + 1 
num += 1

# Comparison Operators, result always return a Boolean (True/False) value
# Equal:                3 == 2      False
# Not Equal:            3 != 2      True     
# Greater than:         3 > 2       True
# Less than:            3 < 2       False
# Greater or Equal:     3 >= 2      True
# Less or Equal:        3 <= 2      False