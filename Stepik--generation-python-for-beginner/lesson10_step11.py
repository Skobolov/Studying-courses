# На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу,
# которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним
# вхождением буквы «h».

# Sample Input 1:
# abch12345h

# Sample Output 1:
# abch54321h


s = input()
print(s[0: s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])