# На вход программе подается строка текста и строка разделитель. Напишите программу, которая вставляет указанный
# разделитель между каждым символом введенной строки текста.

lst = input()
sim = input()

a = lst.split(sim)
for i in a:
    print(sim.join(i))