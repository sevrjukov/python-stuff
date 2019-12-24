# hlavni program
# nacist vstup od uzivatele (matice oddelene operatory, vstup ukoncen zadanim rovnitka
operator = ""
matrices_list = []
operators_list = []
while operator != "=":
    m = int(input("zadejte cislo "))
    matrices_list.append(m)
    operator = input("Zadejte operaci (+/-/*): ")
    if operator != "=":
        operators_list.append(operator)

# vyhodnoceni
# nejdriv redukujeme vsechny operace nasobeni

reduced_matrices_list = [matrices_list.pop(0)]
reduced_operators_list = []
while len(matrices_list) > 0:
    operator = operators_list.pop(0)
    if operator != "*":
        reduced_matrices_list.append(matrices_list.pop(0))
        reduced_operators_list.append(operator)
    else:
        m1 = reduced_matrices_list.pop()
        m2 = matrices_list.pop(0)
        reduced_matrices_list.append(m1 * m2)

# ted projdeme redukovany seznam zleva doprava a aplikujeme operace
result = reduced_matrices_list.pop(0)
for operator in reduced_operators_list:
    if operator == '+':
        result = result + reduced_matrices_list.pop(0)
    elif operator == "-":
        result = result - reduced_matrices_list.pop(0)
    else:
        raise Exception("chyba vstupu, neznamy operator")

print (result)