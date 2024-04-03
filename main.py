from linear import add_matrices

print('''Options:
1. Exponentiation
2. Quotient & Modulus
3. String Operations
4. Lists and matrix addition''')

operation_number = int(input().strip())

x = 9

# Exponentiation
if operation_number == 1:
    print(x ** 2)
    print("{value}^2 = {squared}\nsquare root of {value} = {root}".format(value=x, squared=x ** 2, root=x ** (1 / 2)))


# Quotient
def operation(operator, operand1, operand2, answer):
    return f'{operand1} {operator} {operand2} = {answer}'


if operation_number == 2:
    qnt = 2
    mod = 2
    print(operation(operator="quotient", operand1=x, operand2=qnt, answer=x // qnt))
    print(operation(operator='modulus', operand1=x, operand2=mod, answer=x % mod))

# string operation
if operation_number == 3:
    print("spam, " * 3)


# Lists
if operation_number == 4:
    matrix_1 = [
        [3, -4],
        [8, 5],
    ]

    matrix_2 = [
        [9, -5],
        [2, -6],
    ]

    print(add_matrices(matrix_1, matrix_2))
