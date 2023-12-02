"""

"""
ip = 0
ine = 0
try:
    lim = int(input("Límit: "))
    for i in range(0, lim):
        if i % 2 == 0:
            ip = ip + i
        else:
            ine = ine + i

    print("si el límit és ", lim, "sumaParells", ip, " i sumaSenars", ine)
except ValueError:
    print("No has introducido un número natural")