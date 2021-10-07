num = int(input())
sum = 0
number_digits = 0
pr_digits = 1
first_digit = 0
digit = num % 10
sum_f_l_digits = 0

while num != 0:
    last_digit = num % 10
    sum += last_digit
    number_digits += 1
    pr_digits = pr_digits * last_digit
    first_digit = last_digit

    num = num // 10
print(sum)
print(number_digits)
print(pr_digits)
print(sum / number_digits)
print(first_digit)
print(first_digit + digit)
