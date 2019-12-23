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

# pak provedeme vyhodnoceni zbyvajicich operaci zleva doprava
print(reduced_operators_list)
print(reduced_matrices_list)

reduced_matrices_list.reverse()

