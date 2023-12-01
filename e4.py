"""
Progarma que crea un tablero de escacs
"""
BLANC = "⬜"
NEGRE = "⬛"
i = 0
for h in range(0, 7):
    for j in range(0, 7):

        if j == 7:
            if (j + h) % 2 == 0:
                print(BLANC, end = "")
            else:
                print(NEGRE, end = "")

        elif (j + h) % 2 == 0:
            print(BLANC)
        elif (j + h) % 2 != 0:
            print(NEGRE)
    print()




