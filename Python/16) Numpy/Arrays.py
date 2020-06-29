import numpy as np


def arrays(arr):
    arr_update = list(map(float, arr))
    x = np.asanyarray(arr_update)
    return x[::-1]


arr = input().strip().split()
result = arrays(arr)
print(result)
