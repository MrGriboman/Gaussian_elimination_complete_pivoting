import numpy as np


def back_substitution(matrix, order):
    cur_x = 0
    x = dict()
    for i in range(matrix.shape[0] - 1, -1, -1):
        sum = 0
        row = matrix[i, :-1]
        b_i = matrix[i, -1]
        print(f'row: {row}, b_i: {b_i}')
        for (index, a) in enumerate(row):
            if index != order[cur_x] and index in x:
                sum += a * x[index]
            print(f'sum: {sum}')
        x[order[cur_x]] = b_i - sum
        cur_x += 1
    x = dict(sorted(x.items()))
    return list(x.values())


def gaussian_elimination_complete_pivot(A, b):
    xs = []
    augmented = np.column_stack((A, b))
    rows = augmented.shape[0]
    for k in range(rows):
        #a_max = np.max(np.abs(augmented[k:rows, :-1]))
        row_index, col_index = np.unravel_index(
            np.argmax(np.abs(augmented[k:rows, :-1]), axis=None),
            augmented[k:rows, :-1].shape
        )
        row_index += k
        a_max = augmented[row_index, col_index]
        xs.append(col_index)

        print(f'row and col: {(row_index, col_index)}')

        # Swap the rows
        print(f'before swap\n{augmented}')
        augmented[[k, row_index]] = augmented[[row_index, k]]
        print(f'after swap\n{augmented}')

        # Perform Gaussian elimination on rows below the first row
        augmented[k] /= a_max
        for i in range(k + 1, rows):
            if not augmented[i, col_index]:
                continue
            factor = augmented[k, col_index] / augmented[i, col_index]
            augmented[i] *= factor
            augmented[i] -= augmented[k]
        print(f'after elimination\n{augmented}')
    return back_substitution(augmented, xs[::-1])


n = int(input("Введите размерность \n"))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Введите строку {i + 1}\n").split())))

b = np.array(list(map(float, input("Введите вектор b\n").split())))
A = np.array(A)

x = gaussian_elimination_complete_pivot(np.copy(A), b)
x_solve = np.linalg.solve(A, b)

print(f'Solve solution:\n{x_solve}')
print(f'checking:\n {A @ x == b}')


