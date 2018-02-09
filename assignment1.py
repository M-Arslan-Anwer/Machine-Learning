import matplotlib.pyplot as plt
import numpy as np

theta_0 = 0
theta_1 = 0
alpha = 0.200

#function for reading data from file.
def housing_dataset(name, mode):
    array_1 = []
    with open(name,mode) as handle:
        for line in handle:
            a,b = map(float,line.strip().split())
            array_1.append((a,b))

    return array_1
area_price = housing_dataset("ML_DataSet.txt","r")
n = len(area_price)
def calculate_error(theta_0,theta_1, n,area_price):
    
    new_val_theta_0 = 0
    new_val_theta_1 = 0
    
    for i in range(n):
        new_val_theta_0 += ( theta_0 + theta_1 *area_price[i][0]) - area_price[i][1]
        new_val_theta_1 += ((theta_0 + theta_1 * area_price[i][0])- area_price[i][1])* area_price[i][0]
        
    return (new_val_theta_0/n, new_val_theta_1/n)

    
def gradient_des():
    
    theta_0_ = 0
    theta_1_ = 0
    list_theta_0 = []
    list_theta_1 = []
    counter = 0
    arraycounter=[]

    while True:
        
        arraycounter.append(counter)
        counter+=1
        error_1,error_2 = calculate_error(theta_0_,theta_1_, n, area_price)
        theta_0_ = theta_0_ - alpha * (error_1)
        theta_1_ = theta_1_ - alpha * (error_2)
        error_1 = abs(error_1)
        error_2 = abs(error_2)
        list_theta_0.append(theta_0_)
        list_theta_1.append(theta_1_)
        print(error_1, "  ",error_2)
        if error_1<=0.01 and error_2 <=0.01:
            print("Value of Theta 0 = ",theta_0_)
            print("Value of Theta 1 = ",theta_1_)
            list_theta_0 = np.asarray(list_theta_0)
            list_theta_1 = np.asarray(list_theta_1)
            plt.figure(figsize=(6,4), dpi=80)
            plt.legend(loc = "best")
            plt.xlabel("Number of Iterations")
            plt.ylabel("Thetha 0( Yellow )     Theta 1( Red )")
            plt.title("Values of Thetas")
            plt.plot(arraycounter,list_theta_0,color = "yellow", linewidth=2.5,label ="theta_0")
            plt.plot(arraycounter,list_theta_1,color = "red",linewidth=2.5,label ="theta_0")
            break
        
    return

gradient_des()