#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:37:45 2022

@author: abhinav
"""
from flask import Flask, render_template, request
import pickle
import numpy as np 
app = Flask(__name__, template_folder="template")

model = pickle.load(open("model-3.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("/index.html")


@app.route("/", methods=["POST"])
def predict():
    if request.method == "POST":

        Credit_Score = int(request.form['CreditScore'])

        Geography = request.form["Geography"]
        if Geography == "France":
            Geography = 5014
        elif Geography == "Spain":
            Geography = 2477
        else:
            Geography = 2509

        Gender = request.form["Gender"]
        if Gender == "Female":
            Gender = 0
        else:
            Gender = 1

        Age = int(request.form["Age"])

        Tenure = int(request.form["Tenure"])

        Balance = float(request.form["Balance"])

        Number_of_products = int(request.form["no_of_products"])

        Credit_card = request.form["Credit_card"]
        if Credit_card == "YES":
            Credit_card = 1
        else:
            Credit_card = 0

        Active_member = request.form["Active_member"]
        if Active_member == "YES":
            Active_member = 1
        else:
            Active_member = 0

        Estimated_salary = float(request.form["estimated_salary"])

        features_input = np.array(
            [Credit_Score, Geography, Gender, Age, Tenure, Balance, Number_of_products, Credit_card, Active_member,
             Estimated_salary]).reshape(1,-1)
      
        
        
        prediction = model.predict(features_input)

        if prediction > 0.5:
            return render_template('/index.html', prediction_text="CUSTOMER EXITED")
        else:
            return render_template('/index.html', prediction_text="CUSTOMER REAMINED")


if __name__ == "__main__":
    app.run(debug=True)



