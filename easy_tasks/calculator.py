first_val = float(input())
second_val = float(input())
operation = str(input())

if second_val == 0 and (operation in ['div', 'mod', '/']):
    print('Деление на 0!')
elif operation == '+':
    print(first_val + second_val)
elif operation == '-':
    print(first_val - second_val)
elif operation == '/':
    print(first_val / second_val)
elif operation == '*':
    print(first_val * second_val)
elif operation == 'mod':
    print(first_val % second_val)
elif operation == 'pow':
    print(first_val ** second_val)
elif operation == 'div':
    print(first_val // second_val)
