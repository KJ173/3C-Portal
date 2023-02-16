import pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__,template_folder='template')
app.secret_key = "secret key"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        bank = request.form['banks']
        f = request.files["file"]
        print(f,bank)
        passed_df = pd.read_csv(f)
        present_df = pd.read_excel('')
    



if __name__ == '__main__':
    app.run(debug=True)