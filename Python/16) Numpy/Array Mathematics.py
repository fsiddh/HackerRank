"""
Basic mathematical functions operate element-wise on arrays. They are available both as operator overloads and as functions in the NumPy module.

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
"""

import numpy as np

array_A = list()
array_B = list()

n, m = [int(i) for i in input().strip().split()]

for elements in range(n):
    np.array(array_A.append(list(map(int, input().strip().split()))))

for elements in range(n):
    np.array(array_B.append(list(map(int, input().strip().split()))))

print(np.add(array_A, array_B))

print(np.subtract(array_A, array_B))

print(np.multiply(array_A, array_B))

print(np.floor_divide(array_A, array_B))

print(np.mod(array_A, array_B))

print(np.power(array_A, array_B))
