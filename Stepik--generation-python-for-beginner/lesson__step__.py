n = int(input())
count = 0

while n >= 25:
    n = n - 25
    count += 1
while n >= 10:
    n = n - 10
    count += 1
while n >= 5:
    n = n - 5
    count += 1
while n >= 1:
    n = n - 1
    count += 1
print(count)