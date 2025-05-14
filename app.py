from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained stacking model
model = joblib.load('final_liquidity_stack_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None, label=None, error=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from form
        price = float(request.form['price'])
        one_hour_change = float(request.form['1h'])
        twenty_four_hour_change = float(request.form['24h'])
        seven_day_change = float(request.form['7d'])
        volume = float(request.form['24h_volume'])
        market_cap = float(request.form['mkt_cap'])
        volatility_score = float(request.form['volatility_score'])

        # Prepare input features
        features = np.array([price, one_hour_change, twenty_four_hour_change, seven_day_change,
                             volume, market_cap, volatility_score]).reshape(1, -1)

        # Predict log liquidity and convert back
        log_prediction = model.predict(features)
        liquidity_pred = np.expm1(log_prediction[0])  # Reverse of log1p

        # Classify liquidity
        if liquidity_pred < 0.05:
            liquidity_label = "Low"
        elif 0.05 <= liquidity_pred <= 0.15:
            liquidity_label = "Medium"
        else:
            liquidity_label = "High"

        return render_template('index.html',
                               prediction=f"{liquidity_pred:.5f}",
                               label=liquidity_label,
                               error=None)

    except Exception as e:
        return render_template('index.html', prediction=None, label=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
