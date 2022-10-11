n = 5
k = 2
lst = [i for i in range(1, n+1)]
count = n
while n > 1:
    for i in lst:
        if str(i).isdigit():
            print('digit')
    n = n - 1

# print(s.isdigit())