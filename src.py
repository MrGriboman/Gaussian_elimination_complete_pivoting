import numpy as np


def gaussian_elimination_complete_pivot(A, b):
    augmented = np.column_stack((A, b))
    for k in range(augmented.shape[0]): 
        a_max = np.max(np.abs(augmented[:, :-1]))
        row_index, col_index = np.unravel_index(np.argmax(np.abs(augmented[:, :-1]), axis=None), augmented[:, :-1].shape)

        # Swap the rows
        print(augmented)    
        augmented[[0, row_index]] = augmented[[row_index, 0]]
        print(augmented)

        # Perform Gaussian elimination on rows below the first row
        augmented[0] /= augmented[0, col_index]
        for i in range(1, augmented.shape[0]):
            augmented[0] / augmented[0, col_index]
            factor = augmented[0, col_index] / augmented[i, col_index] 
            augmented[i] *= factor
            augmented[i] -= augmented[0, col_index]                
        print(augmented)


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


