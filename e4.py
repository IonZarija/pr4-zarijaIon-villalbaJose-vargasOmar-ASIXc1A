"""
Progarma que crea un tablero de ajedrez
"""
BLANC = "  "
NEGRE = "██"

for h in range(0, 9):
    for j in range(0, 8):
        if h == 8 and j == 0:
            print(" ", chr(97 + j), end="")
        elif h == 8 and j != 0:
            print("", chr(97 + j), end="")
        else:
            if j == 0:
                if (j + h) % 2 != 0:
                    print(8-h, BLANC, end="")
                elif (j + h) % 2 == 0:
                    print(8-h, NEGRE, end="")
            else:
                if (j + h) % 2 != 0:
                    print(BLANC, end="")
                elif (j + h) % 2 == 0:
                    print(NEGRE, end="")
    print()
