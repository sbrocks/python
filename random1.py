import numpy as np
a=np.random.randn(5,1)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a.T,a))

b=np.random.randn(3,3)
c=np.random.randn(3,1)
d=b*c
print(d.shape)


