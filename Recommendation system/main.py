from flask import Flask, render_template, request
from mynotebook import predictor

app = Flask(__name__)
@app.route('/')
def funct_one():
    return render_template("Webpage.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    user_text = ' '.join(request.form.values())
    print(type(user_text))
    output = predictor(user_text)
    return render_template('Webpage.html', pred=' {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
