import pandas as pd
import math
import numpy as np
from sklearn import preprocessing, cross_validation,neighbors
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df=pd.read_csv('airfoil_self_noise.dat')
##print(df.head())


X=np.array(df.drop(['pres'],1))
y=np.array(df['pres'])

X=preprocessing.scale(X)

X_train, X_test, y_train, y_test= cross_validation.train_test_split(X, y,test_size=0.2)
clf=neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
acc=clf.score(X_test,y_test)
print(acc)
