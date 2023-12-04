"""
Ion Zarija, Omar Vargas, José A. Villalba
ASIXc 1A
M03 UF1 Pr4
"""
h = int(input("Alçada?: "))
y=1
for i in range(0, h):
    if i == h-1:
        print(h*str(h), " "*(h), end="")
    elif h > i>  0:
        print(i+1, " "*(i-1), i+1 ,end="")
    elif i == 0:
        print(y*"1", end="")
    print()