# Принимает два списка чисел, выводит один список отсортированных чисел
# объявление функции
def merge(list1, list2):
    # lst = []
    # for i in list1:
    #     lst.append(int(i))
    # for j in list2:
    #     lst.append(int(j))
    # lst.sort()
    # return lst
    return sorted(list1 + list2, key=int)

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))