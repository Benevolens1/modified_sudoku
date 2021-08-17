from random import randint
from copy import deepcopy

"""
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

def verify_column(matrix:list, y:int)->bool:
    """check if the y column of matrix follows correctly the rules ;
    0 is considered as a jocker."""
    
    present_symbols = []
    
    for i in range(4):
        symbol = matrix[i][y]
        if symbol == 0:
            continue
        if symbol not in present_symbols:
            present_symbols.append(symbol)
        else:
            return False

    return True


def verify_line(matrix:list, x:int)->bool:
    """check if the x line of matrix follows correctly the rules ;
    0 is considered as a jocker."""
    
    present_symbols = []
    
    for i in range(4):
        symbol = matrix[x][i]
        if symbol == 0:
            continue
        if symbol not in present_symbols:
            present_symbols.append(symbol)
        else:
            return False

    return True

        
def verify(matrix:list, a:int, x:int, y:int)->bool:
    """verify if it is possible the element a at coordinates x, y
    given the already placed elements in the current column and line."""
    
    matrix_test = deepcopy(matrix)
    matrix_test[x][y] = a

    result = verify_line(matrix_test, x) and verify_column(matrix_test, y)

    return result


def create(size:int)->list:
    """create a matrix (size*size) following the rules"""

    symbols = [i for i in range(1,size+1)]
    matrix = [[0 for i in range(size)] for i in range(size)]

    for x in range(size):
        for y in range(size):
            tested_symbols = []
            rdm_symbol = randint(1, size)
            tested_symbols.append(rdm_symbol)

            while not verify(matrix, rdm_symbol, x, y):
                rdm_symbol = randint(1, size)
                
                if rdm_symbol in tested_symbols and not verify(matrix, rdm_symbol, x, y):
                    if len(tested_symbols) == size:#this matrix cannot respect the rules
                        print("please restart the program")
                        quit()
                    continue
                
                tested_symbols.append(rdm_symbol)

            tested_symbols = []

            matrix[x][y] = rdm_symbol

    return matrix


def remove(matrix:list, size:int, k:int):
    """place randomly exactly k zeros in the matrix"""

    places = []
    i = 0
    while i < k:
        x = randint(0,size-1)
        y = randint(0,size-1)
        
        if (x, y) not in places:
            places.append((x, y))
            matrix[x][y] = 0
            i+=1

        else:
            continue


test = create(4)

print("")
print("Resolved matrix :")
for i in test:
    print(i)


remove(test, 4, 6)

print("")
print("Matrix to complete :")
for i in test:
    print(i)