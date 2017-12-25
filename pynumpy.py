import numpy as np 
a=np.array([1,2,3])
print(type(a))
print(a[0],a[1],a[2])
print(a.shape)

b=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])
c=b[:2,1:3]
print(b)
print(c)

d=np.ones((3,4))
print(d)

e=np.zeros((2,3))
print(e)

f=np.random.random((3,4))
print(f)

g=np.eye(3)
print(g)
print(g.shape)

print(np.add(d,f))
print(d+f)

print(np.sqrt(f))
print(np.sum(d,axis=1))
print(np.sum(d))
x=np.array([[1,2,3],[4,5,6]])
y=np.array([1,0,1])
print(x+y)
print(x)
print(x.T)








