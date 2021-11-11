# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только
# уникальные строки, в том же порядке, в котором они были введены.

n = int(input())
num = []
num_2 = []

for _ in range(n):
    num.append(input())
for i in num:
    if i in num_2:
        continue
    else:
        num_2.append(i)
print(*num_2, sep='\n')


# dat = []
# for _ in range(int(input())):
#     el = input()
#     if el not in dat:
#         dat.append(el)
#         print(el)
