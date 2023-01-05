import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = pd.read_csv("car.csv",names=['Buying','Persons','lug_boot','doors','safety','class'])
data.head()
data.info()
data['class'],class_name=pd.factorize(data["class"])
print(class_name)
print(data['class'].unique())
data['Buying'],_=pd.factorize(data["Buying"])
data['Persons'],_=pd.factorize(data["Persons"])
data['lug_boot'],_=pd.factorize(data["lug_boot"])
data['doors'],_=pd.factorize(data["doors"])
data['safety'],_=pd.factorize(data["safety"])
data.head()
data.info()
X = data.iloc[:,:4].values
Y = data.iloc[:,4].values
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
dtree = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(X_train,Y_train)
Y_pred =dtree.predict((X_test))
accuracy = (accuracy_score(Y_test,Y_pred))
print("Accuracy",accuracy)
count_misclassified =(Y_test != Y_pred).sum()
print("misclassified",count_misclassified)






