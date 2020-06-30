import numpy

l = list(map(int, input().split()))
result = numpy.reshape(l, (3, 3))
result.shape = (3, 3)
print(result)

result.