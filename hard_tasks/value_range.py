try:
    natur_val = int(input())
    num_degree = int(input())
except ValueError:
    print('Не то вводишь')
else:
    if (natur_val ** natur_val) <= num_degree:
        print(f"Число {natur_val} входит в указанный диапазон")
    else:
        print(f"Число {natur_val} не входит в указанный вами диапазон")
