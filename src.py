import numpy as np

def gaussian_elimination_complete_pivot(A, b):
    augmented = np.column_stack((A, b))
    a_max = np.max(np.abs(A))
    a_max_i = np.argmax(np.abs(A))
    print(a_max, a_max_i)

    num_rows, num_cols = A.shape
    row_index = a_max_i // num_cols
    col_index = a_max_i % num_cols

    # Swap the rows
    print(A)
    A[[0, row_index]] = A[[row_index, 0]]
    print(A)

    # Perform Gaussian elimination on rows below the first row
    for i in range(1, A.shape[0]):
        factor = A[0, col_index] / A[i, col_index] 
        A[i] *= factor
        A[i] -= A[0, col_index]
    print(A)

n = int(input("Введите размерность \n"))
A = []
for i in range(n):
    A.append(list(map(float, input(f"Введите строку {i + 1}\n").split())))

b = np.array(list(map(float, input("Введите вектор b\n").split())))
A = np.array(A)

x = gaussian_elimination_complete_pivot(A, b)
x_solve = np.linalg.solve(A, b)
#print(f"Solution:\n{x}")
#print(f'Solve solution:\n{x_solve}')


