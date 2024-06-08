"""list1=[1,2,3,4,5,6]
list2=[]
import numpy as np

for number in list1:
    list2.append(number**2)

print(list2)

#using matplotlib to make a sine wave
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)
#create the plot
plt.plot(x,y)

#naming the axes
plt.xlabel("x")
plt.ylabel("sinx")

#give a title to this graph
plt.title("Sine Wave")

#show our plot
plt.show()
"""
import numpy as np

dataset_raw=np.genfromtxt("C:/Users/sanja/Desktop/SOC-Deep-Learning/04_Logistic_Regression/dataset/heart.csv", dtype="str", delimiter=",") 
#note that it took my fucking 5 mins straight to get this code run or to import this csv file. 
#coz we want an absolute file path in "_" shit, with forward slash(not backward).
print(dataset_raw.shape)
#print(dataset_raw) this will print the complete table oc, means like headers 2st then all the numbers n all. like we r running em each separately.
#lets name all the headers
headers=dataset_raw[0,:] #here 0 means the 0th line of the csv file, or the headers line, in order to print all the headers. and what ": " means, as its in the y cood position, it means that complete line is selected.(like (inclusive_start:exclusive_end))

print(headers)

#now we get all the numerical data n cast em as float data type instead of str
dataset=dataset_raw[1:,:] #means starts with the first line till the last, and each line completely selected.
dataset=dataset.astype(str)
print(dataset)

#In this dataset, the first 13 columns represent the features, while the 14th column indicates whether the individual has the disease or not based on those features. Here we seperate the dataset into X (feature vector) and Y (output vector).
X = dataset[:, :13]
Y = dataset[:, 13] #this selects the 14th column whole.
print(X.shape)
print(Y.shape)
#but we want the shape of X to be (nx,m)
X = X.T #this gives the value of X of its transpose
print(X.shape) #(nx,m)
print(Y.shape)

print(X.shape[0]) #13
print(X.shape[1]) #since X.shape has become a tuple, so index 1, is 1025
#as of now, nx=13, ny=1, m=1025
#Let's keep 80% of the data for training and 20% of the data for testing our model
# get index to split data in 80:20 ratio

#we create an index, at 80:20 point
index=int(0.8*(X.shape[1]))

#split the data
X_train=X[:,:index] #since X is of the form (nx,m) or (13,1025) where m is the number of training examples
X_test=X-X_train

Y_train=Y[:,:index] 
Y_test=Y-Y_train

print("X_train shape", X_train.shape)
print("Y_train shape", Y_train.shape)
print("Number of training examples =", Y_train.shape[0])
print("-"*40)
print("X_test shape", X_test.shape)
print("Y_test shape", Y_test.shape)
print("Number of testing examples =", Y_test.shape[0])

#LOGISTIC REGRETION