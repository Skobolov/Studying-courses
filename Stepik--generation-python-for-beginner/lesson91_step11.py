# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек),
# если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).


s = input()

for c in s:
    if c in '012456789':
        print('Цифра')
        break
else:
    print('Цифр нет')