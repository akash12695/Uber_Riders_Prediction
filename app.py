#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from flask import Flask,request,render_template
import pickle
import math

#Instantiate the Flask app

app=Flask(__name__)
model=pickle.load(open('taxi.pkl','rb'))        #it is used to load the model

@app.route('/')                                 #Home directory
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]    #int_features is a list
    final_features = [np.array(int_features)]                 #Coverting list into array
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)                          #Rounding off the output till 2 points after decimal

    return render_template('index.html', prediction_text='Number of weekly rides should be {}'.format(math.floor(output)))
   

#if we want to run this app then we should call run function 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)                      #Till the time you are in development mode you have to be in debug mode

