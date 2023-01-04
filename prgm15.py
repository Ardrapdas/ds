import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
student=pd.read_csv('student_scores.csv')
student.head()
X=student.iloc[:,:-1]
Y=student.iloc[:,1]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
print(X_train)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
print(regressor.intercept_)
print(regressor.coef_)
Y_pred=regressor.predict(X_test)
for(i,j) in zip (Y_test,Y_pred):
    if i!=j:
        print("Actual value:",i,"predicted value:",j)
        print("Number of misplaced points from the test dataset:",(Y_test!=Y_pred).sum())
from sklearn import metrics
print("Mean Absolute error:",metrics.mean_absolute_error(Y_test,Y_pred))
print("Mean Squared error:",metrics.mean_squared_error(Y_test,Y_pred))
print("Root Mean Squared error:",np.sqrt(metrics.mean_squared_error(Y_test,Y_pred)))