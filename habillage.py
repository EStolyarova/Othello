
lst_of_lst = [[2]*8 for i in range (8)]

l0 = "  une nouvelle chaine de caracteres "
l1 = "   +---+---+---+---+---+---+---+---+"
l2 = " 1 |   |   |   |   |   |   |   |   |"
l3 = "   +---+---+---+---+---+---+---+---+"
l4 = " 2 |   |   |   |   |   |   |   |   |"
l5 = "   +---+---+---+---+---+---+---+---+"
l6 = " 3 |   |   |   |   |   |   |   |   |"
l7 = "   +---+---+---+---+---+---+---+---+"
l8 = " 4 |   |   |   |   |   |   |   |   |"
l9 = "   +---+---+---+---+---+---+---+---+"
l10 = " 5 |   |   |   |   |   |   |   |   |"
l11 = "   +---+---+---+---+---+---+---+---+"
l12 = " 6 |   |   |   |   |   |   |   |   |"
l13 = "   +---+---+---+---+---+---+---+---+"
l14 = " 7 |   |   |   |   |   |   |   |   |"
l15 = "   +---+---+---+---+---+---+---+---+"
l16 = " 8 |   |   |   |   |   |   |   |   |"
l17 = "   +---+---+---+---+---+---+---+---+"

toto = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17]
bord = "\n".join(toto)
print(bord)


lines = [2, 4, 6, 8, 10, 12, 14, 16]
colonnes = [5, 9, 13, 17, 21, 25, 29, 31]
values = ['X', 'O', ' ']
print(bord)

lst_of_lst[0][1] = 1
lst_of_lst[5][2] = 1
lst_of_lst[6][3] = 0
lst_of_lst[5][4] = 0
lst_of_lst[0][5] = 1

print("\n".join(["".join(str(elem)) for elem in lst_of_lst]))

"""

to_change = [(0, 1, 1), (5, 2, 1), (6, 3, 0), (5, 4, 0), (0, 5, 1)]

for ele in to_change:
    print(ele[0], ele[1], ele[2])
    print(lines[ele[0]]) # = values[ele[2]]
"""
"""bord = "\n".join([l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17])
print(bord)"""


