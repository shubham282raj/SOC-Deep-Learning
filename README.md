# Introduction to Deep Learning

## Season of Code 2024

### MNIST Dataset Neural Network from scratch using NumPy

Link to Kaggle Competition on this dataset [here](https://www.kaggle.com/competitions/digit-recognizer/overview)  
Each image in the dataset is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. 42K train images and 28K test images.  
Epochs trained = 10000, learning rate = 0.1.  
I made use of the functions related to neural network explored in the Week3 assignments and applied it to the MNIST dataset which contains handwritten digits.  
Implemented one_hot_encoding, forward_prop, back_prop, update_params and gradient_descent to make the model work. Also uploaded my predicted y on the test.csv to kaggle to measure the test accarcy. And I got the following accuracies:

`Train Accuracy: 94.97%`  
`Cross validation accuracy: 92.80%`  
`Test Accuracy(on kaggle): 93.035%`  

Cost Function graph:  
<img src="https://github.com/user-attachments/assets/888ac423-85da-4a84-80e1-d07dbed399f2" width="500" height="500">

Prediction of my model on a subset of the dataset.  
![image](https://github.com/user-attachments/assets/d8e56226-f132-4e07-b907-5776669e286d)

