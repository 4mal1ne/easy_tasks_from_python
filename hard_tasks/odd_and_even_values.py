val_number = input()
try:
    convert_val = int(val_number)
except ValueError:
    print('Число мне дай')

even_val = 0
odd_val = 0

while convert_val > 0:
    if convert_val % 2 == 0:
        even_val += 1
    else:
        odd_val += 1
    convert_val = convert_val // 10
print(f'чётные числа:  {even_val}, нечётные числа: {odd_val}')
