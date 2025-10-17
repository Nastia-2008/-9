import numpy as np
N = int(input("Введіть розмір квадратного масиву N: "))
A = np.arange(1, N**2 + 1).reshape(N, N)
print("масив:\n", A)

sum_d = sum(A[i][N - 1 - i] for i in range(N))
print("Сума елементів допоміжної діагоналі:", sum_d)

max = np.max(A, axis=1)
print("Найбільші елементи кожного рядка:", max)
