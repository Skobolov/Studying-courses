a, b = input(), input()

if (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
    if a == 'красный':
        if b == 'красный':
            print('красный')
        elif b == 'синий':
            print('фиолетовый')
        elif b == 'желтый':
            print('оранжевый')
    elif a == 'синий':
        if b == 'красный':
            print('фиолетовый')
        elif b == 'синий':
            print('синий')
        elif b == 'желтый':
            print('зеленый')
    elif a == 'желтый':
        if b == 'красный':
            print('оранжевый')
        elif b == 'синий':
            print('зеленый')
        elif b == 'желтый':
            print('желтый')
else:
    print('ошибка цвета')
