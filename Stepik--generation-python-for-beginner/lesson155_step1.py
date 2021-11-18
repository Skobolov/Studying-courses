#           ШИФР ЦЕЗАРЯ

# t1 = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# t2 = "абвгдежзийклмнопрстуфхцчшщъыьэюя АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# eng_lower_alphabet = [chr(i) for i in range(97, 123)]
# eng_upper_alphabet = [chr(i) for i in range(65, 91)]
# rus_lower_alphabet = [chr(i) for i in range(1072, 1104)]
# rus_upper_alphabet = [chr(i) for i in range(1040, 1072)]


def shifr_cezar(direction, lang, k, text):
    lst = []
    if lang == 1:
        for i in text:

            if i.islower() and i.isalpha():
                if direction == 1:
                    if ord(i) + k > 122:
                        lst.append(chr((97 + ((ord(i) + k) - 123))))
                    else:
                        lst.append(chr(ord(i) + k))
                else:
                    if ord(i) - k < 97:
                        lst.append(chr((123 - (97 - (ord(i) - k)))))
                    else:
                        lst.append(chr(ord(i) - k))

            elif i.isupper() and i.isalpha():
                if direction == 1:
                    if ord(i) + k > 90:
                        lst.append(chr(65 + ((ord(i) + k) - 91)))
                    else:
                        lst.append(chr(ord(i) + k))
                else:
                    if ord(i) - k < 65:
                        lst.append(chr(91 - (65 - (ord(i) - k))))
                    else:
                        lst.append(chr(ord(i) - k))
            else:
                    lst.append(i)

    if lang == 2:
        for i in text:

            if i.islower() and i.isalpha():
                if direction == 1:
                    if ord(i) + k > 1103:
                        lst.append(chr((1072 + ((ord(i) + k) - 1104))))
                    else:
                        lst.append(chr(ord(i) + k))
                else:
                    if ord(i) - k < 1072:
                        lst.append(chr((1104 - (1072 - (ord(i) - k)))))
                    else:
                        lst.append(chr(ord(i) - k))

            elif i.isupper() and i.isalpha():
                if direction == 1:
                    if ord(i) + k > 1071:
                        lst.append(chr(1040 + (ord(i) + k) - 1072))
                    else:
                        lst.append(chr(ord(i) + k))
                else:
                    if ord(i) - k < 1040:
                        lst.append(chr(1072 - (1040 - (ord(i) - k))))
                    else:
                        lst.append(chr(ord(i) - k))
            else:
                lst.append(i)

    return print(*lst, sep='')


# direction = int(input('Направление шифрования: 1 - шифр, 2 - дешифр: '))
# lang = int(input('Язык: 1 - анг, 2 - ру: '))
# k = int(input('Шаг сдвига: '))
# text = input('Введите текст: ')


# shifr_cezar(direction, lang, k, text)

def sdet():
    for i in range(1, 26):
        print(shifr_cezar(1, 1, i, 'Day, mice. "Year" is a mistake!'), i)


sdet()

