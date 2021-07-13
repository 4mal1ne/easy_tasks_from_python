check_proger = int(input())

if check_proger % 10 == 1 and check_proger % 100 != 11:
    print(check_proger, 'программист')
elif check_proger % 10 in [2, 3, 4] and check_proger % 100 not in [12, 13, 14]:
    print(check_proger, 'программиста')
else:
    print(check_proger, 'программистов')
