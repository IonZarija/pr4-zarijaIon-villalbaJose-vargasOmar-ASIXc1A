"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
Programa que al introducir una cantidad de números enteros, devuelve la cantidad de positivos,negativos y zeros
"""
ip = 0
ine = 0
try:
    lim = int(input("Límite: "))
    for i in range(0, lim):
        if i % 2 == 0:
            ip = ip + i
        else:
            ine = ine + i

    print("si el límit és ", lim, "sumaParells", ip, " i sumaSenars", ine)
except ValueError:
    print("No has introducido un número natural")