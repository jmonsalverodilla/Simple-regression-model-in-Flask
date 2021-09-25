#Imports
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Read the data
data = pd.read_csv(".dat/Expenses_Prediction.csv")
print(data.shape)
print("Hola")

#Scale the data
scaler = MinMaxScaler() 
data_scaled = scaler.fit_transform(data)
df = pd.DataFrame.from_records(data_scaled)

##X matrix and target
X = df.iloc[:,:2]
Y= df.iloc[:,-1]

#Train a really simple model without any kind of tuning
lr_model = LinearRegression()
lr_model.fit(X, Y)

#Get R2 in train! This should actually be done with an independent test since otherwise the result will be overfitted
Y_predict = lr_model.predict(X)
r2 = r2_score(Y, Y_predict)
print('R2 score is {}'.format(r2))

# Saving model to disk
#pickle.dump(lr_model, open('lr_model.pkl','wb'))
joblib.dump(lr_model, "lr_model.pkl")