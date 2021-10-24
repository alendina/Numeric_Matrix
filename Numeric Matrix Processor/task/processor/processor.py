import copy


def matrix_input(n, m):
    matrix = [[float(x) for x in input().split()] for _ in range(int(n))]
    return matrix


def matrix_output(matrix):
    # print("\n".join(" ".join(str(x) for x in row_) for row_ in matrix))
    matrix_format = [["{:6.3f}".format(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
    print('The result is:')
    for x in matrix_format:
        print(*x)


def matrix_add(x_matrix, y_matrix):
    z_matrix = []
    for i in range(len(x_matrix)):
        row_ = [x_matrix[i][j] + y_matrix[i][j] for j in range(len(x_matrix[i]))]
        z_matrix.append(row_)
    return z_matrix


def matrix_multiple_const(matrix, const):
    matrix = [[const * matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return matrix


def matrix_multiply(x_matrix, y_matrix):
    # Zn,k=Xn,m×Ym,k .
    nz_row = len(x_matrix)     # row Z
    kz_col = len(y_matrix[0])  # col Z
    m_xy = len(y_matrix)
    z_matrix = []
    for nz in range(nz_row):
        row_z = []
        for kz in range(kz_col):
            row_xn = x_matrix[nz]
            col_yk = [y_matrix[i][kz] for i in range(m_xy)]
            dot = sum([row_xn[i] * col_yk[i] for i in range(m_xy)])
            row_z.append(dot)
        z_matrix.append(row_z)
    return z_matrix


def transpose_main_diagonal(matrix):
    t_matrix = []
    for i in range(len(matrix[0])):
        ti_row = [matrix[j][i] for j in range(len(matrix))]
        t_matrix.append(ti_row)
    return t_matrix


def transpose_side_diagonal(matrix):
    matrix = matrix[::-1]
    t_matrix = transpose_main_diagonal(matrix)
    t_matrix = t_matrix[::-1]
    return t_matrix


def transpose_vertical_line(matrix):
    t_matrix = [matrix[i][::-1] for i in range(len(matrix))]
    return t_matrix


def transpose_horizontal_line(matrix):
    t_matrix = matrix[::-1]
    return t_matrix


def determinant(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        return 'The matrix is not a square matrix'
    else:
        if n <= 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        elif n > 2:
            det = 0
            for i in range(n):
                i_matrix = copy.deepcopy(matrix)
                del i_matrix[0]
                for row in i_matrix:
                    del row[i]
                # matrix_output(i_matrix)
                det += ((-1) ** i) * matrix[0][i] * determinant(i_matrix)
                # print(det)
            return det


def inverse(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n != m:
        return 'The matrix is not a square matrix'
    else:
        if n <= 1:
            return matrix[0][0]
        elif n == 2:
            # inverse = (1 /(a*d - c*b)) * matrix((d,-b), (-c,a))
            co = [[matrix[1][1], - matrix[0][1]], [- matrix[1][0], matrix[0][0]]]
            invert = matrix_multiple_const(co, 1 / (matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]))
            return invert
        elif n > 2:
            det = determinant(matrix)
            # print('det =', det)
            if det == 0:
                return "This matrix doesn't have an inverse."
            else:
                co = []
                for j in range(n): # row
                    i_co = []
                    for i in range(n): # col
                        i_matrix = copy.deepcopy(matrix)
                        del i_matrix[j]
                        for row in i_matrix:
                            del row[i]
                        # matrix_output(i_matrix)
                        # print(f'(i,j) = (row {j},col{i}) and det = {determinant(i_matrix)} and matrix_ji = {matrix[j][i]}')
                        # matrix_output(i_matrix)
                        i_co.append(((-1) ** (i + j) * determinant(i_matrix)))
                    co.append(i_co)
                co = transpose_main_diagonal(co)
                invert = matrix_multiple_const(co, 1 / det)
                return invert


# ----------
while True:
    print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    choice = input('Your choice: ')

    if choice == '1':  # Add matrices
        n1, m1 = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        a = matrix_input(int(n1), int(m1))
        n2, m2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        b = matrix_input(int(n2), int(m2))
        if n1 == n2 and m1 == m2:
            c = matrix_add(a, b)
            matrix_output(c)
        else:
            print('The operation cannot be performed.')

    elif choice == '2':  # Multiply matrix by a constant
        n1, m1 = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        a = matrix_input(int(n1), int(m1))
        c = input('Enter constant: ')
        d = matrix_multiple_const(a, float(c))
        matrix_output(d)

    elif choice == '3':  # Multiply matrices
        n1, m1 = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        a = matrix_input(int(n1), int(m1))
        n2, m2 = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        b = matrix_input(int(n2), int(m2))
        if m1 == n2:
            c = matrix_multiply(a, b)
            matrix_output(c)
        else:
            print('The operation cannot be performed.')

    elif choice == '4':  # Transpose matrix
        print('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        choice_t = input('Your choice: ')
        n1, m1 = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        a = matrix_input(int(n1), int(m1))
        if choice_t == '1':    # Transposition along the main diagonal
            t = transpose_main_diagonal(a)
        elif choice_t == '2':  # Transposition along the side diagonal
            t = transpose_side_diagonal(a)
        elif choice_t == '3':  # Transposition along the vertical line
            t = transpose_vertical_line(a)
        elif choice_t == '4':  # Transposition along the horizontal line
            t = transpose_horizontal_line(a)
        else:
            t = []
        matrix_output(t)

    elif choice == '5':  # Calculate a determinant
        n1, m1 = input('Enter matrix size: ').split()
        if m1 == n1:
            print('Enter matrix:')
            a = matrix_input(int(n1), int(m1))
            print('The result is:')
            print(determinant(a))
        else:
            print('The operation cannot be performed.')

    elif choice == '6':  # Inverse matrix
        n1, m1 = input('Enter matrix size: ').split()
        if m1 == n1:
            print('Enter matrix:')
            a = matrix_input(int(n1), int(m1))
            v = inverse(a)
            matrix_output(v)
            # matrix_output(matrix_multiply(a, v))
            # matrix_output(matrix_multiply(v, a))
        else:
            print('The operation cannot be performed.')

    elif choice == '0':  # Exit
        exit()
