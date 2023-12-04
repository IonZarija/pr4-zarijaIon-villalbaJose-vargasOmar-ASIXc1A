"""

"""
h=int(input("Alçada?: "))
sp = 1
while h >= 10:
    h=int(input("Alçada?: "))
for i in range(1,h+1):
    if 2 < i < h:
        print(i, " "*sp, i)
        sp = sp+2
    elif i == 1:
        print(i)
    elif i == 2:
        print(i, i)
    elif i == h:
        for x in range(i):
            print(i, sep = " ", end =" ")
