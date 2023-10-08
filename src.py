import numpy as np


def gaussian_elimination_complete_pivot(A, b):
    augmented = np.column_stack((A, b))
    rows = np.copy(augmented.shape[0]) #maybe copy
    for k in range(rows):         
        a_max = np.max(np.abs(augmented[k:rows, :-1]))
        row_index, col_index = np.unravel_index(
            np.argmax(np.abs(augmented[k:rows, :-1]), axis=None),
            augmented[k:rows, :-1].shape
        )
        row_index += k

        print(f'row and col: {(row_index, col_index)}')

        # Swap the rows
        print(f'before swap\n{augmented}')    
        augmented[[k, row_index]] = augmented[[row_index, k]]
        print(f'after swap\n{augmented}')

        # Perform Gaussian elimination on rows below the first row
        augmented[k] /= a_max
        for i in range(k + 1, rows):
            augmented[k] / a_max
            if not augmented[i, col_index]:
                continue
            factor = a_max / augmented[i, col_index]
            augmented[i] *= factor
            augmented[i] -= a_max              
        print(f'after ellimination\n{augmented}')


n = int(input("Введите размерность \n"))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Введите строку {i + 1}\n").split())))

b = np.array(list(map(float, input("Введите вектор b\n").split())))
A = np.array(A)

x = gaussian_elimination_complete_pivot(np.copy(A), b)
x_solve = np.linalg.solve(A, b)
#print(f"Solution:\n{x}")
#print(f'Solve solution:\n{x_solve}')


