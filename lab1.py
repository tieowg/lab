python
import math

l1 = (2.591 * (0.836 * (1/3))) / math.sqrt(1.147 * (math.e*2 + math.e**-2))
l2 = 3 * (math.sqrt(-1 * math.log10(0.8 * 10*4)))

if abs(l1) < 1 + abs(l2):
    u = (3 * l1 - 512) / (l1*2 + l2*2)
    print(u)
elif abs(l1) >= 1 + abs(l2):
    u = (3 * l1 + 512) / (l1*2 - l2*2)
    print(u)
