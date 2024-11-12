import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'
threshold = 0.45

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('bank-marketing')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    subscribe = y_pred >= threshold

    result = {
        'subscribe_probability': float(y_pred),
        'subscribe_decision': bool(subscribe)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)