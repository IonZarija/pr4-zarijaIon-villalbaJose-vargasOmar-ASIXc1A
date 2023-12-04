"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Progama que al introducirle dos valores, devuelve su multiplicación
"""
num1 = int(input("Introduce el primer valor de la multiplicación"))
num2 = int(input("Introduce el segundo valor de la multiplicación"))
res = 0
try:
    for x in range(0, num1):
        res = res + num2
except ValueError:
    print("No has introducido un número natural")
print(res)
