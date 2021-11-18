# Аве, Цезарь
# Sample Input 1:
# Day, mice. "Year" is a mistake!
# Sample Output 1:
# Gdb, qmgi. "Ciev" ku b tpzahrl!


def ave_cezar(text):
    lst = []
    for i in text.split():
        count = 0
        for z in i:
            if z.isalpha():
                count += 1
        for j in i:

            if j.islower() and j.isalpha():
                if ord(j) + count > 122:
                    lst.append(chr((97 + ((ord(j) + count) - 123))))
                else:
                    lst.append(chr(ord(j) + count))

            elif j.isupper() and j.isalpha():
                if ord(j) + count > 90:
                    lst.append(chr(65 + ((ord(j) + count) - 91)))
                else:
                    lst.append(chr(ord(j) + count))

            else:
                lst.append(j)

        lst.append(' ')

    return print(*lst, sep='')


ave_cezar(input())





