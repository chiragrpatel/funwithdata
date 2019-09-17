import numpy as np

alist = [1,2,3,4,5,6,7]

print(alist)


npalist = np.array(alist)

print(npalist)

data = np.random.randn(2,3)

print(data)

print(data.shape)
print(data.ndim)
print(data.dtype)

rangelist = list(range(10))

print(rangelist)