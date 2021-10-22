s = input()
c_l = 0
for c in s:
    if c in s.lower and s.isalpha() == True:
        c_l += 1
print(c_l)