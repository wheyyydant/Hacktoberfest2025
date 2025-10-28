d1, d2, d3 = map(int, input().split())

w = (d1 + d2 + d3)
x = (d1 + d2)*2
y = (d2 + d3)*2
z = (d1 + d3)*2

if x <= y and x <= z and x <= w:
    print(x)
elif y <= x and y <= z and y <= w:
    print(y)
elif z <= y and z <= x and z <= w:
    print(z)
else:
    print(w)
