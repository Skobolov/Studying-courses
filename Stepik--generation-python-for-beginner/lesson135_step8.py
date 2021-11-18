# Функция принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль
# является действительным паролем BEEGEEK
#   Действительный пароль BEEGEEK банка имеет вид a:b:c
#   число a – должно быть палиндромом;
#   число b – должно быть простым;
#   число c – должно быть четным.



# объявление функции
def is_valid_password(password):
    lst = password.split(':')
    count, countf, countpr = 0, 0, 0
    for i in password:
        if i.isalpha():
            count += 1
    if count > 0 or len(lst) != 3:
        return False
    else:
        for i in range(3):
            if i == 0:
                if lst[0] == lst[0][::-1]:
                    countf += 1
                else:
                    return False
            elif i == 1:
                if int(lst[1]) == 1:
                    return False
                else:
                    for i in range(2, int(lst[1])):
                        if int(lst[1]) % i == 0:
                            countpr += 1
                    if countpr == 0:
                        countf += 1
        if int(lst[2]) % 2 == 0:
            countf += 1
        if countf == 3:
            return True
        else:
            return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
