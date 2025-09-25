from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return render_template('metrics.html')

@app.route('/calculators')
def calculators():
    return render_template('calculators.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/psychology')
def psychology():
    return render_template('psychology.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    calc_type = data.get('type')

    if calc_type == 'position_size':
        account_size = float(data.get('accountSize', 0))
        risk_percentage = float(data.get('riskPercentage', 0))
        stop_loss = float(data.get('stopLoss', 0))

        risk_amount = account_size * (risk_percentage / 100)
        position_size = risk_amount / stop_loss if stop_loss > 0 else 0

        return jsonify({
            'riskAmount': round(risk_amount, 2),
            'positionSize': round(position_size, 0),
            'maxLoss': round(risk_amount, 2)
        })

    elif calc_type == 'risk_reward':
        entry_price = float(data.get('entryPrice', 0))
        stop_loss = float(data.get('stopLoss', 0))
        target_price = float(data.get('targetPrice', 0))

        risk = abs(entry_price - stop_loss)
        reward = abs(target_price - entry_price)
        ratio = reward / risk if risk > 0 else 0

        return jsonify({
            'risk': round(risk, 2),
            'reward': round(reward, 2),
            'ratio': round(ratio, 2)
        })

    elif calc_type == 'kelly_criterion':
        win_rate = float(data.get('winRate', 0)) / 100
        avg_win = float(data.get('avgWin', 0))
        avg_loss = float(data.get('avgLoss', 0))

        if avg_loss > 0:
            b = avg_win / avg_loss
            p = win_rate
            q = 1 - p
            kelly_percentage = ((b * p - q) / b) * 100 if b > 0 else 0
            kelly_percentage = max(0, min(kelly_percentage, 25))  # Cap at 25% for safety
        else:
            kelly_percentage = 0

        return jsonify({
            'kellyPercentage': round(kelly_percentage, 2),
            'suggestedAllocation': round(kelly_percentage * 0.5, 2)  # Half Kelly for safety
        })

    return jsonify({'error': 'Invalid calculation type'}), 400

if __name__ == '__main__':
    app.run(debug=True)