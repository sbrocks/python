import numpy as np
A=np.array([[56.0,0.0,4.4,68.0],
			[1.2,104.0,52.0,8.0],
			[1.8,135.0,99.0,0.9]])

print(A)
cal=A.sum(axis=0)    //sums elements of matrix A vertically
print(cal)
percentage=100*A/cal.reshape(1,4)
print(percentage)

B=np.array([1,2,3,4])
print(A+B)

print(A.shape)   //gives size of matrix A