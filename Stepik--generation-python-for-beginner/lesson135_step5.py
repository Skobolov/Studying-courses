#   Надежность пароля
#   - его длина не менее 8 символов
#   - он содержит как минимум одну заглавную букву (верхний регистр)
#   - он содержит как минимум одну строчную букву (нижний регистр)
#   - он содержит хотя бы одну цифру

# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    c1, c2, c3 = 0, 0, 0

    for i in password:
        if i.isdigit():
            c1 += 1
        if i.isalpha() and i == i.upper():
            c2 += 1
        if i.isalpha() and i == i.lower():
            c3 += 1

    if c1 > 0 and c2 > 0 and c3 > 0:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))