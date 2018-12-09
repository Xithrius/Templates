c = int(input())
g = 1
p = 0
while c >= g:
    c = c - g
    g = g + 1
    p = p + 1
    print(c, g, p)

print(p)