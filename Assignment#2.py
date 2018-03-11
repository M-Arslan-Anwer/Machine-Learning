
#		Assignment No 2
# 		Logistic Regression


import numpy as np

def segmoid_function(X):
	return (1.0 / (1 + np.exp(-X)) )

def prediction(x,y,w,b):

	for i in range(500):
		z = np.dot(w,x[i].T)+b
		a = segmoid_function(z)
		label = 0 if a <0.5 else 1
		print("prediction={}       actual={}".format(label, y[0][i]))
	

# Logistic Regression Main Function

def regression_function():
	b = 1
	half = 750 																			# for using half of the data 
	alpha = 0.05																		
	
	data = np.genfromtxt("adult1.csv",delimiter=',')
	print(data[0][1])
	np.random.shuffle(data)
	
	test_data,train_data = data[:half:,:],data[half:,:]
	
	data_X,data_Y = train_data[:,:-1],train_data[:,-1]
	
	data_Y = np.array([data_Y])
	data_X = data_X.T
	
	
	weight = np.array([0.5,0.4,0.2,0.1])
	weight = np.array(weight)
	
	
	for i in range(5000):
		data_Z = np.dot(weight,data_X) + b
		
		data_A = segmoid_function(data_Z)
		
		dz = data_A - data_Y
		error = np.sum(dz**2)
		
		dw = np.dot(data_X,data_Z.T)/(np.prod(data_X.shape))
		db = np.sum(dz) / (np.prod(data_X.shape))
		
		weight -= alpha*dw.T
		b -= alpha*(db)
		
	new_data_X, new_data_Y = test_data[:,:-1],test_data[:,-1]
	new_data_Y = np.array([new_data_Y])
	prediction(new_data_X,new_data_Y,weight,b)
	
regression_function()

	