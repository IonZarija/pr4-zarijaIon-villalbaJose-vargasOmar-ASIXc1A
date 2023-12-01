"""

"""
num = 0
null = 0
pos = 0
res = 0
for x in range(0,9):
    num = int(input("Introduce una número: "))
    if num == 0:
        null = null + 1
    elif num > 0:
        pos = pos + 1
    elif num < 0:
        res = res + 1
print("Has introducido ",null, " zeros",",", pos, "números positivos, y finalmente, ",res," números negativos")


