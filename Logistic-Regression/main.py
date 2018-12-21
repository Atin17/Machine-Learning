import pandas as pd
import random
import numpy as np
from sklearn import cross_validation, preprocessing
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv('bezdekIris.csv')

##randmize dataset
##import from sklearn.utils import shuffle
##df = df.shuffle(df)

df = df.sample(frac=1).reset_index(drop=True)
print(df.head())


X = np.array(df.drop(['c'],1))
y = np.array(df['c'])
encoder = preprocessing.LabelEncoder()
y = encoder.fit_transform(y)
print(y)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)
print(accuracy)

Xp = np.array([[15.3,56.3,10.5,1.3]])

print(clf.predict(Xp))

plt.scatter(df['c'], df['sl'],)
plt.xlabel('category')
plt.ylabel('len')
plt.show()
