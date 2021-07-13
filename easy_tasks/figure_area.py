figure = input()

if figure == 'треугольник':
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    s = (val_a + val_b + val_c) / 2
    print((s * (s - val_a) * (s - val_b) * (s - val_c)) ** 0.5)
elif figure == 'прямоугольник':
    val_a = float(input())
    val_b = float(input())
    print(val_a * val_b)
elif figure == 'круг':
    val_a = float(input())
    print(3.14 * (val_a ** 2))
