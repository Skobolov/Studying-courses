# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит их
# местами и выведет на экран.
# Если длина строки нечетная, то длина первой части должна быть на один символ больше.


s = input()
s1 = 1

if int(len(s)) % 2 == 0:
    s1 = int(int(len(s)) / 2)
else:
    s1 = int((int(len(s)) / 2) + 1)

print(s[s1:] + s[:s1])