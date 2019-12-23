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

    def load_from_input_fast(self):
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
    def load_from_std_input(self):
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

    # odecte dve matice
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
                    s = s + self.matrix_values[n][i] * self.matrix_values[i][j]
                d.append(s)
                s = 0
            result_values.append(d)
            d = []
        result_matrix = Matrix()
        result_matrix.set_values(result_values)
        return result_matrix

    def main(self, other):
        operace = input("Znak operaci (+/-/*): ")
        self.print_m(self.matrix_values)
        print(operace)
        other.print_m(other.matice)
        print("=")
        print()
        if operace == "*":
            if self.s != other.r:
                print("Error. Chybny vstup!")
            else:
                self.__mul__(other)
                self.print_m(self.__mul__(other))
        elif operace == "+":
            if self.r != other.r and self.s != other.s:
                print("Error. Chybny vstup!")
            else:
                self.__add__(other)
                self.print_m(self.__add__(other))
        else:
            if self.r != other.r and self.s != other.s:
                print("Error. Chybny vstup!")
            else:
                self.__sub__(other)
                self.print_m(self.__sub__(other))


# hlavni program
# vytvoreni a nacteni prvni matice
m1 = Matrix()
m1.load_from_input_fast()
m1.print_m()

m2 = Matrix()
m2.load_from_input_fast()
m2.print_m()

m3 = m1.__mul__(m2)
m3.print_m()
