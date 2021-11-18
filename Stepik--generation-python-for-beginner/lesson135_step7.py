# Функция принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом
# и False в противном случае.
# При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.


# объявление функции
def is_palindrome(text):
    lst = []
    for i in text:
        if i.isalpha():
            lst.append(i.lower())
    if lst[:] == lst[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))