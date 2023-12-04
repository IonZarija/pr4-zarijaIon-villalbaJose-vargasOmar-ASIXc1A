"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Progama que al introducirle dos valores, devuelve su multiplicación
"""
try:
    num1 = int(input("Introduce el primer valor de la multiplicación"))
    num2 = int(input("Introduce el segundo valor de la multiplicación"))
    res = 0
    while num1 < 0 or num2 < 0:
        num1 = int(input("Introduce el primer valor positivo de la multiplicación"))
        num2 = int(input("Introduce el segundo valor positivo de la multiplicación"))

    for x in range(0, num1):
        res = res + num2

    print(res)
except ValueError:
    print("No has introducido un número natural")

