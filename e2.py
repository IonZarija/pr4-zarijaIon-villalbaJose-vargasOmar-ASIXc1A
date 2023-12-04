"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Programa que hace una pirámide
"""
try:
    h = int(input("Alçada?: "))
    while h >= 10 or h < 0:
        h = int(input("Alçada?: "))
    y=1
    for i in range(1,h+1):
        if i == h:
            for x in range(h):
                print(i, sep=" ", end=" ")
        elif h > i > 2:
            print(i, y*" ", i, end ="")
            y += 2
        elif i == 1:
            print(i, end="")
        elif i == 2:
            print(i, i, end="")
        print()
except ValueError:
    print("No has introducido un valor numerico")