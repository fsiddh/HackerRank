"""
1) identity:-
The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as
  and the rest as . The default type of elements is float.

import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

2) eye:-
The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main,
upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower
, and a (default) is for the main diagonal.

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.
"""

import numpy as np

n, m = [int(i) for i in input().strip().split()]
result = np.eye(n, m)
print(str(result).replace('1', ' 1').replace('0', ' 0'))