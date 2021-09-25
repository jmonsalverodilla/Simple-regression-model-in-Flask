#Imports
import numpy as np
from flask import Flask,render_template,request
import joblib
import os

#Flask
app = Flask(__name__)
model = joblib.load("lr_model.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_expenses',methods=['POST'])
def predict_expenses():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted monthly grocery expenses $ {}'.format(output))

if __name__ == "__main__":
    port = os.environ.get("PORT", 8080)
    app.run(debug=True, host="0.0.0.0", port=port)

