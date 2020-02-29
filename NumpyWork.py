import numpy as np
import _random

i = 0
j = 0
k = 0
arry = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arry.shape)
awq = np.array([[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]])
print(awq.shape)
print(awq)
x, y, z = awq.shape
for i in range(x):
    for j in range(y):
        for k in range(z):
            print(awq[i][j][k], "=", i, j, k)

dizi = np.zeros((1, 20), dtype=np.int8)
for r in range(1):
    for s in range(20):
        dizi[r][s] = 1

print(dizi)
