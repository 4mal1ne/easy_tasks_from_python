try:
    simple_val = int(input())
except ValueError:
    print('А можно число, пжлст ?')
else:
    if simple_val > 1 and (simple_val % 1 == 0 and simple_val % simple_val == 0):
        print(f'{simple_val} - это простое число')
    else:
        print(f'{simple_val} не является простым числом')
