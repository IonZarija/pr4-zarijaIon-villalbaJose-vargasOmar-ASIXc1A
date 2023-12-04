"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Progama que al introducirle dos valores enteros, devuelve su multiplicación
"""
try:
    num1 = int(input("Introduce el primer valor de la multiplicación"))
    num2 = int(input("Introduce el segundo valor de la multiplicación"))
    res = 0

    if num1 < 0 and num2 < 0:
        num1 = -num1
        num2 = -num2
        for x in range(0, num1):
            res = res + num2
    elif num1 < 0:
        for x in range(0, num2):
            res = res + num1
    elif num2 < 0:
        for x in range(0, num1):
            res = res + num2
    print(res)
except ValueError:
    print("No has introducido un carácter numérico")
