"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Programa que cuenta cuantos numeros positivos, negativos o zeros has introducido
"""
num = 0
null = 0
pos = 0
res = 0
i = 0
try:
    vol = int(input("Quantos números desea introducir"))
    while i < vol:
        num = int(input("Introduce una número: "))
        if num == 0:
            null = null + 1
        elif num > 0:
            pos = pos + 1
        elif num < 0:
            res = res + 1
        i = i + 1
except ValueError:
    print("No has introducido un número natural")

print("Has introducido ", null, " zeros", ",", pos, "números positivos, y finalmente ", res, " números negativos")

