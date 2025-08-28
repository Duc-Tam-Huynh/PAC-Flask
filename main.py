import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model1 = pickle.load(open('randomforest.pkl', 'rb'))
model2 = pickle.load(open('randomforest.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_td',methods=['POST', 'GET'])
def predict_td():
    '''
    For rendering results on HTML GUI
    '''
    #if request.method == 'POST':
    nhietDo = request.form['nhietDo']
    pH = request.form['pH']
    doDuc = request.form['doDuc']
    doMau = request.form['doMau']
    chatLoLung = request.form['chatLoLung']
    doDan = request.form['doDan']
    #int_features = [float(x) for x in request.form.values()]
    int_features = [float(nhietDo), float(pH), float(doDuc), float(doMau), float(chatLoLung), float(doDan)]
    final_features = [np.array(int_features)]
    prediction = model1.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text=f' {output:.2f} mg/L')

@app.route('/predict_th',methods=['POST'])
def predict_th():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)

    output = prediction[0]

    return render_template('indexth.html', prediction_text=f' {output:.2f} mg/L')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model1.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
