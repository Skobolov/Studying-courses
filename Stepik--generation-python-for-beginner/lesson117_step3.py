keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda']

new_keywords_1 = [i[1::] for i in keywords]     #содержащий строки исходного списка с удаленным первым символом
print(new_keywords_1)

lengths = [len(i) for i in keywords]    #содержащий длины строк исходного списка
print(lengths)

new_keywords_2 = [i for i in keywords if len(i) > 4]    #содержащий только слова длиной не менее пяти символов
print(new_keywords_2)

palindromes = [i for i in range(100, 1000) if i % 10 == i // 100]   #список всех чисел палиндромов от 100 до 1000
print(palindromes)

kub_keywords = [int(i) ** 3 for i in input().split()]     #подается строка текста, содержащая целые числа.
for i in kub_keywords:                                    #вывод кубов указанных чисел в строку
    print(i, end=' ')

print(*[i for i in input().split()], sep='\n')      #выводит слова введенной строки в столбик

print(*[i for i in input() if i.isdigit()], sep='')     #выводит все цифровые символы введенной строки

#подается строка целых чесел через пробел. вывод квадрата четных чисел, которые не оканчиваются на цифру 4
print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])
