# На вход программе подается натуральное число n >= 2, а затем n целых чисел. Напишите программу, которая создает
# из указанных чисел список, состоящий из сумм соседних чисел

lst = []
lst_sum = []
s = int(input())

for _ in range(s):
    lst.append(int(input()))
for i in range(1, s):
    lst_sum.append(lst[i-1] + lst[i])
print(lst_sum)
