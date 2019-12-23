class Matrix():

    # konstruktor
    def __init__(self):
        self.matrix_values = []
        self.r = 0
        self.s = 0

    def set_values(self, matrix_values):
        self.matrix_values = matrix_values
        self.r = len(matrix_values)
        self.s = len(matrix_values[0])

    def read_from_input_fast(self):
        matrix_string = input("Zadejte hodnoty matice, radky oddelene teckou: ")
        lines = matrix_string.split(".")
        self.r = len(lines)
        for line_string in lines:
            line_string = line_string.strip()
            current_line = []
            elements = line_string.split(" ")
            self.s = len(elements)
            for element in elements:
                current_line.append(int(element))
            self.matrix_values.append(current_line)

    # nacte matici ze standardniho vstupu
    def read_from_input(self):
        self.r = int(input("Zadejte pocet radku: "))
        self.s = int(input("Zadejte pocet sloupcu: "))

        for i in range(self.r):
            a = []
            for j in range(self.s):
                a.append(int(input("Zadejte clen na {0},{1} posici: ".format(int(i + 1), int(j + 1)))))
            self.matrix_values.append(a)

    # vypise matici do standardniho vystuou
    def print_m(self):
        print(str(len(self.matrix_values)) + " X " + str(len(self.matrix_values[0])), end="\n")
        for i in range(len(self.matrix_values)):
            for j in range(len(self.matrix_values[0])):
                print("{:3d}".format(self.matrix_values[i][j]), end=" ")
            print()

    # secte dve matice, vrati novou matici obsahujici soucet
    def __add__(self, other):
        result_values = []
        if self.r != other.r or self.s != other.s:
            raise Exception("chyba vstupu, matice nemaji stejnou velikost")

        for i in range(0, self.r):
            current_line = []
            for j in range(0, self.s):
                current_line.append(self.matrix_values[i][j] + other.matrix_values[i][j])
            result_values.append(current_line)

        result_matrix = Matrix()
        result_matrix.set_values(result_values)
        return result_matrix

    # odecte dve matice, vrati novou matici
    def __sub__(self, other):
        result_values = []
        if self.r != other.r or self.s != other.s:
            raise Exception("chyba vstupu, matice nemaji stejnou velikost")

        for i in range(0, self.r):
            current_line = []
            for j in range(0, self.s):
                current_line.append(self.matrix_values[i][j] - other.matrix_values[i][j])
            result_values.append(current_line)

        result_matrix = Matrix()
        result_matrix.set_values(result_values)
        return result_matrix

    # vynasobi dve matice, vrati novou matici
    def __mul__(self, other):
        if self.s != other.r:
            raise Exception("chyba vstupu, matice nemaji spravnou velikost")
        s = 0
        d = []
        result_values = []
        s2 = other.s  # sloupce 2m

        for n in range(0, self.r):
            for j in range(0, s2):
                for i in range(0, self.s):
                    s = s + self.matrix_values[n][i] * other.matrix_values[i][j]
                d.append(s)
                s = 0
            result_values.append(d)
            d = []
        result_matrix = Matrix()
        result_matrix.set_values(result_values)
        return result_matrix


# hlavni program
# nacist vstup od uzivatele (matice oddelene operatory, vstup ukoncen zadanim rovnitka
operator = ""
matrices_list = []
operators_list = []
while operator != "=":
    m = Matrix()
    m.read_from_input()
    matrices_list.append(m)
    operator = input("Zadejte operaci (+/-/*/=): ")
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
        reduced_matrices_list.append(m1.__mul__(m2))

# ted projdeme redukovany seznam zleva doprava a aplikujeme operace
result = reduced_matrices_list.pop(0)
for operator in reduced_operators_list:
    if operator == '+':
        result = result.__add__(reduced_matrices_list.pop(0))
    elif operator == "-":
        result = result.__sub__(reduced_matrices_list.pop(0))
    else:
        raise Exception("chyba vstupu, neznamy operator")

m.print_m()
