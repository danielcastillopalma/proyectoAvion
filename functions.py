import numpy as np
def avionVacio():
    cont = 1
    emptyPlane = np.zeros((7,6), dtype = int)
    for i in range(7):
        for j in range(6):
            emptyPlane[i][j] = cont
            cont = cont+1
    for i in range(7):
        for j in range(6):
            if j == 0:
                print((f"|\t {emptyPlane[i][j]}\t"), end = "")
            if j != 0 and j!= 5 and j!= 2:
                print((emptyPlane[i][j]), end = "\t")
            if j == 2:
                print ((emptyPlane[i][j]), end = "\t\t")
            if j == 5:
                print(f"{emptyPlane[i][j]}\t|")
            if i == 4 and j == 5:
                print("|_________________________\t\t________________________|")
                print("|_________________________\t\t________________________|")
            if i == 5 and j == 5:
                print("|                         \t\t                        |")
                