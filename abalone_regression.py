import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,HuberRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,hinge_loss
from sklearn.preprocessing import normalize
df=pd.read_csv(r'C:\Users\Ariya Rayaneh\Desktop\abalone.csv')

x=df.drop(['Sex','Rings'],axis=1)
y=df.Rings
print(normalize(x))
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
yy_pred=model.predict([[0.475,0.37,0.125,0.5,0.216,0.112,0.16]])
score=model.score(x_train,y_train)
mbe=mean_absolute_error(y_test,y_pred)
print(mbe)
mse=mean_squared_error(y_test,y_pred)
print(mse)
def hinge_loss(y_true, y_pred, sample_weight):
  margin = y_true * y_pred
  loss = np.maximum(0, 1 - margin)
  print(np.average(loss, weights=sample_weight))

sample_weight = np.random.rand(len(y_test))
hinge_loss(np.squeeze(y_test), np.squeeze(y_pred), sample_weight)


model1=HuberRegressor()
model1.fit(x_train,y_train)
y1_pred=model1.predict(x_test)
score1=model1.score(x_train,y_train)
mse1=mean_squared_error(y_test,y1_pred)

print(mse1)