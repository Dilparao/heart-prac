# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:04:59 2020

@author: Dilba
"""


from flask import Flask, request, render_template
import os
import pickle

print(os.getcwd())
path = os.getcwd()



# with open('Models/dt.pkl', 'rb') as f:
#     dt_model = pickle.load(f)

# with open('Models/lr.pkl', 'rb') as f:
#     logistic_model = pickle.load(f)

# with open('Models/svm_linear.pkl', 'rb') as f:
#     svm_linear_model = pickle.load(f)

# with open('Models/svm_poly.pkl', 'rb') as f:
#     svm_poly_model = pickle.load(f)
    
with open('Models/svm_rbf.pkl', 'rb') as f:
    svm_rbf_model = pickle.load(f)

# with open('Models/xgb.pkl', 'rb') as f:
#     xgb_model = pickle.load(f)


def get_predictions(age, weight, ap_hi, ap_lo, cholesterol, gluc, bmi, req_model):
    mylist = [age, weight, ap_hi, ap_lo, cholesterol, gluc, bmi]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

#     if req_model == 'Logistic':
#         #print(req_model)
#         return logistic_model.predict(vals)[0]

#     elif req_model == 'DecisionTree':
#         #print(req_model)
#         return dt_model.predict(vals)[0]

#     elif req_model == 'SvmLinear':
#         #print(req_model)
#         return svm_linear_model.predict(vals)[0]
    
#     elif req_model == 'SvmPoly':
#         #print(req_model)
#         return svm_poly_model.predict(vals)[0]
    
    if req_model == 'SvmRbf':
        #print(req_model)
        return svm_rbf_model.predict(vals)[0]    
    
#     elif req_model == 'Xgboost':
#         #print(req_model)
#         return xgb_model.predict(vals)[0]    
    else:
        return "Cannot Predict"


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    age = request.form['age']
    weight = request.form['weight']    
    ap_hi = request.form['ap_hi']
    ap_lo = request.form['ap_lo']
    cholesterol=request.form['cholesterol']
    gluc = request.form['gluc']
    bmi = request.form['bmi']
    req_model = request.form['req_model']
    target = get_predictions(age, weight, ap_hi, ap_lo, cholesterol, gluc,bmi, req_model)

    if target==1:
        disease_present = 'Patient is likely to have heart disease'
    else:
        disease_present = 'Patient is unlikely to have heart disease'

    return render_template('home.html', target = target, disease_present = disease_present)


if __name__ == "__main__":
    app.run(debug=True)