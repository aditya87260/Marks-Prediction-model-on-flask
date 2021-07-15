import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
"""""
X=pd.read_csv("Linear_X_Train.csv")
Y=pd.read_csv("Linear_Y_Train.csv")
plt.scatter(X,Y)
plt.show()
model=LinearRegression(normalize=True)
model.fit(X,Y)
print(model.predict([[2.5]]))

from sklearn.externals import joblib

joblib.dump(model,"model.pkl")

"""""
m=joblib.load("model.pkl")
print(m.predict([[2.5]]))
