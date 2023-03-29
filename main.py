# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model =pickle.load(open('Review.pkl','rb'))


@app.route('/')
def funct_one():
    return render_template("Webpage.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    user_text=request.form.values()
    output=model.predict(user_text)
    return render_template('Webpage.html', pred=' {}'.format(output[0]))
if __name__ == '__main__':
    app.run(debug=True)