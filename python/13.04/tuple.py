a = 'aaaa'
b = 'bbbb'

t = a
a = b
b = t

b, a = (a, b)

print(a)  # ==> bbbb
print(b)  # ==> aaaa