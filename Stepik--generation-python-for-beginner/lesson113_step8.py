# Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', ...
# Последний элемент списка состоит из 26 символов z

a = []
for i in range(1, 27):
    a.append(chr(96 + i) * i)
print(a)