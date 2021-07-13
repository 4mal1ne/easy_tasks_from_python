first_natur_val = int(input())
second_natur_val = int(input())
third_natur_val = int(input())

arithmetic_mean = (first_natur_val + second_natur_val) / 3
geometric_mean = pow(second_natur_val, 1. / first_natur_val)

print(f'The arithmetic mean = {arithmetic_mean}')
print(f'The geometric mean = {geometric_mean}')
