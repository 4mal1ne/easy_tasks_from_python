step_count = 0

step_list = {
    'step_1': '1',
    'step_2': '2',
    'step_3': '3',
    'step_4': '4',
    'step_5': '5',
    'step_6': '6'
}

while five_l_bucket != 4:
    step = input()
    try:
        step == ' ' or step == type(str)
    except ValueError:
        print(f'ты ввёл мне {step}, а нужна цифра... ')

    if step == step_list['step_1']:
        step_count += 1
        five_l_bucket = 5
        print(f'{step_count} шаг: \t')
        print(end=f'\rпятилитровое ведро равно {five_l_bucket} литрам')
    elif step == step_list['step_2']:
        step_count += 1
        three_l_bucket = five_l_bucket - 2
        five_l_bucket -= 3
        print(end=f'\r{step_count} шаг: пятилитровик равен {five_l_bucket}, трёхлитровик равен {three_l_bucket}')
    elif step == step_list['step_3']:
        step_count += 1
        three_l_bucket -= three_l_bucket
        print(end=f'\r{step_count} шаг: пятилитровик равен {five_l_bucket}, трёхлитровик равен {three_l_bucket}')
    elif step == step_list['step_4']:
        step_count += 1
        three_l_bucket = five_l_bucket
        five_l_bucket -= five_l_bucket
        print(end=f'\r{step_count} шаг: пятилитровик равен {five_l_bucket}, трёхлитровик равен {three_l_bucket}')
    elif step == step_list['step_5']:
        step_count += 1
        five_l_bucket = 5
        print(end=f'\r{step_count} шаг: пятилитровик равен {five_l_bucket}, трёхлитровик равен {three_l_bucket}')
    elif step == step_list['step_6']:
        step_count += 1
        three_l_bucket += 1
        five_l_bucket -= 1
        print(end=f'\r{step_count} шаг: пятилитровик равен {five_l_bucket}, трёхлитровик равен {three_l_bucket}')
    else:
        print('Шото не то')
        break

    if five_l_bucket == 4 and step_count == 6:
        print(f'\nПоздравляю! Ты сделал это и твоё ведро равно {five_l_bucket} литрам!')
    elif step_count > 6 and five_l_bucket < 4:
        print('у тебя всего 6 ходов')
        break
    elif five_l_bucket == 4 and step_count < 6:
        print('\nменьше чем за 6 ходов ты не решишь, даже не пытайся!!')
