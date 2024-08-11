# Matrix v1.0.0
# Programmer: Ilia Abbasi

import os
from typing import Self

def remove_zero(val : int | float) -> int | float:
    if val == int(val):
        return int(val)
    return val

class Matrix_Error(Exception):
    def __init__(self, message):
        self.message = message

class Matrix:
    a = []
    m = 0
    n = 0

    def __init__(self, a : list[list] | int) -> None:
        if type(a) is int:
            a = [[a]]
        
        self.m = len(a)
        if self.m == 0:
            self.n = 0
        else:
            self.n = len(a[0])
        
        self.a = a
    
    def __add__(self, matrix2 : Self | int | float) -> Self:
        if not (type(matrix2) is Matrix):
            matrix2 = Matrix([[matrix2]])
        
        if self.m != matrix2.m:
            raise Matrix_Error("Unequal row number. Addition is impossible.")
        if self.n != matrix2.n:
            raise Matrix_Error("Unequal column number. Addition is impossible.")
        
        result = Matrix.Zero(self.m, self.n)

        for i in range(result.m):
            for j in range(result.n):
                result.a[i][j] = self.a[i][j] + matrix2.a[i][j]
        
        return result

    def __sub__(self, matrix2 : Self | int | float) -> Self:
        if not (type(matrix2) is Matrix):
            matrix2 = Matrix([[matrix2]])

        if self.m != matrix2.m:
            raise Matrix_Error("Unequal row number. Subtraction is impossible.")
        if self.n != matrix2.n:
            raise Matrix_Error("Unequal column number. Subtraction is impossible.")
        
        result = Matrix.Zero(self.m, self.n)

        for i in range(result.m):
            for j in range(result.n):
                result.a[i][j] = self.a[i][j] - matrix2.a[i][j]
        
        return result

    def __mul__(self, matrix2 : Self | int | float) -> Self:
        if not (type(matrix2) is Matrix):
            return self.mul_with_number(matrix2)
        
        if self.n != matrix2.m:
            raise Matrix_Error("Multiplication is not possible.")
        
        result = Matrix.Zero(self.m, matrix2.n)

        for i in range(result.m):
            for j in range(result.n):
                for index in range(self.n):
                    result.a[i][j] += self.a[i][index] * matrix2.a[index][j]

        return result
    
    def __eq__(self, matrix2 : Self | int | float) -> bool:
        if not (type(matrix2) is Matrix):
            if self.m != 1 or self.n != 1:
                return False
            return self.a[0][0] == matrix2
        
        if self.m != matrix2.m or self.n != matrix2.n:
            return False

        for i in range(self.m):
            for j in range(self.n):
                if self.a[i][j] != matrix2.a[i][j]:
                    return False
        
        return True
    
    def __ne__(self, matrix2 : Self | int | float) -> bool:
        return not self.__eq__(matrix2)
    
    def __str__(self) -> str:
        return str(self.a)
    
    def for_print_string(self) -> str:
        if self.m == 0 or self.n == 0:
            return ""

        result = ""

        for i in range(self.m):
            for j in range(self.n):
                result += str(remove_zero(round(self.a[i][j], 5))) + ", "
            result += "\n"
        
        result = result[:-3]
        
        return result

    def Zero(m : int, n : int = -1) -> Self:
        if n == -1:
            n = m
        
        return Matrix.Full(m, n, 0)
    
    def Full(m : int, n : int, val) -> Self:
        a = []

        for i in range(m):
            a.append([])
            for j in range(n):
                a[i].append(val)
        
        return Matrix(a)

    def I(n : int) -> Self:
        return Matrix.Scalar(n, 1)
    
    def Scalar(n : int, val) -> Self:
        matrix = Matrix.Zero(n, n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    matrix.a[i][j] = val
        
        return matrix
    
    def add_row(self, m : int, row : list) -> Self:
        if m < 0:
            raise Matrix_Error("Invalid row number.")
        if m > self.m:
            m = self.m
        
        if len(row) != self.n:
            raise Matrix_Error("Invalid row size.")
        
        a = list(self.a)

        a.insert(m, row)

        return Matrix(a)
    
    def add_column(self, n : int, column : list) -> Self:
        if n < 0:
            raise Matrix_Error("Invalid column number.")
        if n > self.n:
            n = self.n
        
        if len(column) != self.m:
            raise Matrix_Error("Invalid column size.")
        
        a = list(self.a)

        for i in range(self.m):
            a[i].insert(n, column[i])

        return Matrix(a)

    def mul_with_number(self, number : int | float) -> Self:
        result = Matrix.Zero(self.m, self.n)

        for i in range(result.m):
            for j in range(result.n):
                result.a[i][j] = self.a[i][j] * number
        
        return result
    
    def submatrix(self, m : int, n : int) -> Self:
        a = []

        for i in range(self.m):
            if i == m:
                continue

            a.append([])
            for j in range(self.n):
                if j == n:
                    continue

                a[-1].append(self.a[i][j])
        
        return Matrix(a)
    
    def transposition(self) -> Self:
        result = Matrix.Zero(self.n, self.m)

        for i in range(self.m):
            for j in range(self.n):
                result.a[j][i] = self.a[i][j]
        
        return result
    
    def cofactor_of(self, i : int, j : int) -> int | float:
        if i >= self.m or j >= self.n:
            raise Matrix_Error("Non-existant entry.")
        return ((-1) ** (i + j)) * self.submatrix(i, j).determinant()
    
    def comatrix(self) -> Self:
        result = Matrix.Zero(self.m, self.n)

        for i in range(result.m):
            for j in range(result.n):
                result.a[i][j] = self.cofactor_of(i, j)
        
        return result

    def determinant(self) -> int | float:
        if self.m != self.n:
            raise Matrix_Error("Can't get determinant of a non-square matrix.")

        if self.m == 0 or self.n == 0:
            return 0
        if self.m == 1 and self.n == 1:
            return self.a[0][0]
        if self.m == 2 and self.n == 2:
            return self.a[0][0] * self.a[1][1] - self.a[0][1] * self.a[1][0]
        
        result = 0

        for j in range(self.n):
            result += self.a[0][j] * self.cofactor_of(0, j)
        
        return result
    
    def adjoint(self) -> Self:
        return self.comatrix().transposition()
    
    def inverse(self) -> Self:
        det = self.determinant()
        if det == 0:
            raise Matrix_Error("Can't get inverse of a matrix with the determinant of 0.")

        return self.adjoint() * (1 / det)



matrixes = {}

def pause(msg : bool = True) -> None:
    if msg:
        input("Successful.")
    else:
        input()

def clear() -> None:
    os.system("cls")

def print_matrix(matrix_name : str) -> None:
    print(matrix_name + " = [")
    print(matrixes[matrix_name].for_print_string())
    print("]\n")

def save_matrix(matrix : Matrix) -> None:
    clear()

    print("[")
    print(matrix.for_print_string())
    print("]\n")

    name = input("Save this matrix as(! to discard): ")

    if name == "!":
        return
    
    matrixes[name] = matrix

    pause()

def menu() -> None:
    print("MATRIXES:")
    for matrix_name in matrixes.keys():
        print_matrix(matrix_name)
    
    print(
'''
1) Create matrix     2) Add matrix
3) Subtract matrix   4) Multiply matrix
5) Get determinant   6) Get inverse
'''
)

    choice = input("\nYour choice: ")
    clear()

    if choice == "1":
        name = input("Matrix name: ")
        m = int(input("Rows = "))
        n = int(input("Columns = "))

        matrix = Matrix.Zero(m, n)

        for i in range(m):
            for j in range(n):
                matrix.a[i][j] = float(input(f"a({i+1}, {j+1}) = "))
        
        matrixes[name] = matrix
        
        pause()
    
    if choice == "2":
        name1 = input("Name of first matrix: ")
        name2 = input("Name of second matrix: ")

        result = matrixes[name1] + matrixes[name2]

        save_matrix(result)
    
    if choice == "3":
        name1 = input("Name of first matrix: ")
        name2 = input("Name of second matrix: ")

        result = matrixes[name1] - matrixes[name2]

        save_matrix(result)
    
    if choice == "4":
        name1 = input("Name of first matrix: ")
        name2 = input("Name of second matrix: ")

        result = matrixes[name1] * matrixes[name2]

        save_matrix(result)
    
    if choice == "5":
        name = input("Name of matrix: ")

        print("\n\n" + f"det({name}) = " + str(remove_zero(matrixes[name].determinant())))

        pause(False)
    
    if choice == "6":
        name = input("Name of matrix: ")

        save_matrix(matrixes[name].inverse())

def main() -> None:
    while True:
        clear()
        menu()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou 'Ctrl-C'ed out of this place!")
    except Matrix_Error as e:
        print(f"Exception caught:\n{e}")
