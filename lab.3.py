x = 0.1
y = 0
a = 1
k = 1
while x**a/a >= 0.01:
    y = y + k*(x**a/a)
    k = -k
    a = a + 1
print (y)
