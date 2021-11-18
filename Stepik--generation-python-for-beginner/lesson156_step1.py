#       Калькулятор систем счисления

def converter_chisel(from_to, sistema_is, numbers):

    lst_16 = ['A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    if from_to == '1':
        numbers = numbers[::-1]

        if sistema_is == '2' or sistema_is == '4' or sistema_is == '8':
            for i in range(len(numbers)):
                count += int(numbers[i]) * (int(sistema_is) ** int(i))

        elif sistema_is == '16':
            for i in range(len(numbers)):
                if numbers[i] in lst_16:
                    a = 10 + lst_16.index(numbers[i])
                else:
                    a = numbers[i]
                count += int(a) * (16 ** int(i))

    if from_to == '2':
        dv_digit = str()
        numbers = int(numbers)

        if sistema_is == '2' or sistema_is == '4' or sistema_is == '8':
            numbers = int(numbers)


            while numbers > 0:
                dv_digit += str(numbers % int(sistema_is))
                numbers //= int(sistema_is)
            count = dv_digit[::-1]

        elif sistema_is == '16':
                while numbers > 0:
                    n = numbers % int(sistema_is)
                    if n >= 10:
                        dv_digit += str(lst_16[int(n) - 10])
                    else:
                        dv_digit += str(n)
                    numbers //= int(sistema_is)
                count = dv_digit[::-1]

    return print(count)


fr_to = input('1 - в десятичную, 2 - из десятичной: ')
sis_is = input('2 - двоичная, 4 - четвертичная система, 8 - восьмеричная, 16 - шестнадцатиричная: ')
num = input('Число: ')

converter_chisel(fr_to, sis_is, num)


