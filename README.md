# Marketcalls - Money Management Tutorial

A professional money management education platform for traders, built with Flask and styled with Tailwind CSS + Preline UI in the Zerodha Varsity style.

## Features

- **Home Page**: Overview of money management principles and why they matter
- **Metrics Page**: Detailed explanations of key trading metrics (Win Rate, Risk-Reward, Sharpe Ratio, etc.)
- **Calculators Page**: Interactive tools for position sizing, risk-reward analysis, and Kelly Criterion
- **Psychology Page**: Van Tharp's revolutionary trading psychology principles and techniques
- **Quotes Page**: Wisdom and insights from legendary traders and market veterans

## Tech Stack

- **Backend**: Flask (Python) - Serverless Functions
- **Frontend**: Tailwind CSS + Preline UI (via CDN)
- **Deployment**: Vercel (Serverless)

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open browser to `http://localhost:5000`

## Deployment to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

Follow the prompts to configure your deployment.

## API Endpoints

- `GET /` - Home page
- `GET /metrics` - Trading metrics explained
- `GET /calculators` - Interactive calculators
- `GET /psychology` - Van Tharp's trading psychology
- `GET /quotes` - Trading wisdom
- `POST /api/calculate` - Calculator API endpoint

## Calculator Types

1. **Position Size Calculator**: Calculate optimal position size based on risk tolerance
2. **Risk-Reward Calculator**: Evaluate trade setups
3. **Kelly Criterion Calculator**: Determine optimal bet sizing

## Educational Content

The platform teaches:
- The 2% Rule for risk management
- Risk-reward ratios and their importance
- Key performance metrics for traders
- Position sizing strategies
- Trading psychology and discipline

## MIT License

Copyright (c) 2024 Marketcalls

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Disclaimer

This application is for educational purposes only and should not be considered as financial advice. Always consult with a qualified financial advisor before making any trading decisions.