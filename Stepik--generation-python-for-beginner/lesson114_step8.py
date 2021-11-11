# На вход подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк —
# поисковые запросы. Напишите пр., которая выводит все введенные строки, в которых встречаются все поисковые запросы.


n = int(input())
num, num_2, num_3 = [], [], []

for _ in range(n):
    num.append(input())
q = int(input())
for _ in range(q):
    num_2.append(input())
for i in num:
    d = 0
    for j in num_2:
        if j.upper() in i.upper():
            d += 1
            if d == len(num_2):
                num_3.append(i)
print(*num_3, sep='\n')