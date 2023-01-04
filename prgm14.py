import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree,metrics,model_selection
data=pd.read_csv('car.csv',names=['buying','maint','doors','persons','lug_boot','safety','class'])
data.head()
data.info()
data['class'],class_names=pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())
data['buying'],_ =pd.factorize(data['buying'])
data['maint'],_ =pd.factorize(data['maint'])
data['doors'],_ =pd.factorize(data['doors'])
data['persons'],_ =pd.factorize(data['persons'])
data['lug_boot'],_ =pd.factorize(data['lug_boot'])
data['safety'],_ =pd.factorize(data['safety'])
data.head()
data.info()
X=data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.3,random_state=0)
dtree =tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(X_train,y_train)
y_pred=dtree.predict(X_test)
accuracy = metrics.accuracy_score(y_test,y_pred)
print('Accuracy:{:.2f}'.format(accuracy))
count_misclassified=(y_test!=y_pred).sum()
print('Misclassified samples:{}'.format(count_misclassified))