import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("D:\csv\Data.csv")
model = LinearRegression()
model.fit(data[['Gender','Height']],data['Weight'])

print(model.predict([[1,179]]))