import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm




dataset = pd.read_csv('houses.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1:].values



   
    
X = np.append(np.ones((7,1)).astype(int),X ,axis = 1)

X_opt = X[:,[2,3,5]]
clf_ols = sm.OLS(endog = y, exog = X_opt).fit()
print(clf_ols.summary())
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2, random_state = 0)
##print (X_test)
##print(y_test)


clf = LinearRegression()
clf.fit(X_train, y_train)

##print(y_pred)
acc = clf.score(X_test,y_test)
print(acc*100)
