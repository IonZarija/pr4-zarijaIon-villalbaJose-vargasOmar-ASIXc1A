"""
Progarma que crea un tablero de escacs
"""
BLANC = "  "
NEGRE = "██"

for h in range(0, 8):
    for j in range(0, 8):

        if (j + h) % 2 != 0:
            print(BLANC, end = "")
        elif (j + h) % 2 == 0:
            print(NEGRE, end = "")
    print()




