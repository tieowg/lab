x = 0.1
y = 0
a = 1
while x**a/a >= 0.01:
    y = y - (-(x**a/a))
    a = a + 1
print (y)
