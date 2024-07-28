c = float(input())

epsilon = 10e-7
func = lambda x: x**2 + x**0.5
l = 1
r = c**3


while l < r - epsilon:
    m = (l + r) / 2
    if func(m) < c:
        l = m
    else:
        r = m

print((l+r)/2)