# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:10:52 2020

@author: gonca
"""


# importing the flask magic
from flask import Flask, render_template, request
from helper import run_model
import time

# Flask Logic section
# here you are creating an object that is a Flask app!
app = Flask(__name__)

# we have to create routes -> a possible door that our app can expect to be open!
# we use decorators to create routes -> called using '@' -> calls a python
# inbuilt function without having to import it

@app.route('/', methods = ['POST', 'GET'])

# for each rote you define one python function to be executed (this will be the result)

def index():
    # the python logic that will be run when the route is called
    if request.method == 'POST':
        
        # do stuff
        parameter_1 = request.form['parameter 1'] # ele ja devolve str
        parameter_2 = str(request.form['parameter 2'])
        parameter_3 = float(request.form['parameter 3'])
        parameter_4 = float(request.form['parameter 4'])
        parameter_5 = float(request.form['parameter 5'])
        parameter_6 = float(request.form['parameter 6'])
        time.sleep(2)
        prediction = [round(run_model(parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6)[0] * 100, 1)]
        
        print('the prediction is ', prediction)
        
        # if we want to eturn the result to our html we needf to pass the
        # variable to the main.html
        
        return render_template('main2.html', predictions = prediction)
    
    else:
        return render_template('main2.html')

# running our flask app defined above
if __name__ == '__main__':
    app.run(debug = True)