import numpy as np
X=np.array([[1,1,1,0],[1,0,1,1],[0,1,0,1]])
y=np.array([[1],[1],[0]])

print(X)
print(y)

def sigmoid(x):
	return 1/(1+np.exp(-x))

def derivatives_sigmoid(x):
	return x*(1-x)

#variable initialization
epoch=5000
lr=0.1
inputlayer_neurons=X.shape[1]
hiddenlayer_neurons=3
output_neurons=1

#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))

print(wh)
print(bh)
print(wout)
print(bout)

for i in range(epoch):
	#forward propagation
	hiddenlayer_input1=np.dot(X,wh)
	hiddenlayer_input=hiddenlayer_input1+bh
	hiddenlayer_activations=sigmoid(hiddenlayer_input)
	outputlayer_input1=np.dot(hiddenlayer_activations,wout)
	outputlayer_input=outputlayer_input1+bout
	output=sigmoid(outputlayer_input)
	
	#backward propagation
	E=y-output
	slope_outputlayer=derivatives_sigmoid(output)
	slope_hiddenlayer=derivatives_sigmoid(hiddenlayer_activations)
	d_output=E*slope_outputlayer
	Error_at_hidden_layer=d_output.dot(wout.T)
	d_hiddenlayer=Error_at_hidden_layer*slope_hiddenlayer
	wout+=hiddenlayer_activations.T.dot(d_output)
	bout+=np.sum(d_output,axis=0,keepdims=True)*lr
	wh+=X.T.dot(d_hiddenlayer)*lr
	bh+=np.sum(d_hiddenlayer,axis=0,keepdims=True)*lr


print(output)






