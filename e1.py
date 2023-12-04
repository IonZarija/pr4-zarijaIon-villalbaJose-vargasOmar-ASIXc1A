"""
Programa que al introducir una cantidad de números enteros, devuelve la cantidad de positivos,negativos y zeros
"""
num = 0
null = 0
pos = 0
res = 0
i = 0
try:
    vol = int(input("Cuantos números desea introducir? "))
    while i < vol:
        num = int(input("Introduce un número: "))
        if num == 0:
            null = null + 1
        elif num > 0:
            pos = pos + 1
        elif num < 0:
            res = res + 1
        i = i + 1
except ValueError:
    print("No has introducido un número natural")

print("Has introducido ", null, " zero/s", ",", pos, "número/s positivo/s, y finalmente ", res, " número/s negativo/s")

