year_check = int(input())

if (year_check % 4 == 0 and year_check % 100 != 0) or year_check % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
