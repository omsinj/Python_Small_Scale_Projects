# Create a function holding the calculation
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# create a dictionary
operations = {
    '+':add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }

num1 = int(input('Whats the first number?: '))
num2 = int(input('Whats the second number?: '))


for symbols in operations:
    print(symbols)

operation_symbol = input('Pick an operation from the line above: ')

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')



# Create a function holding the calculation
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square_root(n1,n2):
    return n1 ** n2

# create a dictionary
operations = {
    '+':add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': square_root
    }

def calculator():
    num1 = int(input('Whats the first number?: '))

    for symbols in operations:
        print(symbols)

    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation from the line above: ')
        num2 = int(input('Whats the next number?: '))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input("Type 'y' to conitunue calculating with {answer} or type 'n' to start a new calculation") == 'y':
            num1 = answer

        else:
           should_continue = False
            break
            calculator()



calculator()
