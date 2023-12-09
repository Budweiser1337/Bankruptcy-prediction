from flask import Flask, request, jsonify
import joblib
import pandas as pd
import traceback
import sys

app = Flask(__name__)

lr = None

@app.route('/predict', methods=['POST'])
def predict():
    global lr

    if lr:
        try:
            json_ = request.json
            print(json_)
            
            # Provide a default index for the DataFrame
            query = pd.DataFrame(json_, index=[0])
            
            # One-hot encode the input data
            query = pd.get_dummies(query)
            
            # Reindex the columns
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12345

    lr = joblib.load("MLPClassifier.pkl")
    print('Model loaded')
    model_columns = joblib.load("model_columns.pkl")
    print('Model columns loaded')

    app.run(port=port, debug=True)

'''
{
    " ROA(C) before interest and depreciation before interest": 0.35,
    " Non-industry income and expenditure/revenue": 0.36,
    " Operating Expense Rate": 0.2,
    " Research and development expense rate": 0.52,
    " Cash flow rate": 0.35,
    " Interest-bearing debt interest rate": 0.63,
    " Net Value Per Share (B)": 0.45,
    " Persistent EPS in the Last Four Seasons": 0.48,
    " Operating Profit Per Share (Yuan ¥)": 0.60,
    " Realized Sales Gross Profit Growth Rate": 0.52,
    " Operating Profit Growth Rate": 0.39,
    " Continuous Net Profit Growth Rate": 0.46,
    " Total Asset Growth Rate": 0.48,
    " Net Value Growth Rate": 0.44,
    " Total Asset Return Growth Rate Ratio": 0.52,
    " Current Ratio": 0.70,
    " Quick Ratio": 0.38,
    " Interest Expense Ratio": 0.48,
    " Debt ratio %": 0.23,
    " Borrowing dependency": 0.42,
    " Accounts Receivable Turnover": 0.24,
    " Inventory Turnover Rate (times)": 0.4,
    " Operating profit per person": 0.32,
    " Allocation rate per person": 0.62,
    " Working Capital to Total Assets": 0.21,
    " Quick Assets/Total Assets": 0.31,
    " Cash/Total Assets": 0.2,
    " Quick Assets/Current Liability": 0.12,
    " Cash/Current Liability": 0.31,
    " Inventory/Working Capital": 0.12,
    " Current Liabilities/Liability": 0.3,
    " Working Capital/Equity": 0.25,
    " Long-term Liability to Current Assets": 0.28,
    " Retained Earnings to Total Assets": 0.33,
    " Total income/Total expense": 0.22,
    " Total expense/Assets": 0.31,
    " Current Asset Turnover Rate": 0.29,
    " Working capital Turnover Rate": 0.47,
    " Cash Turnover Rate": 0.41,
    " Equity to Long-term Liability": 0.28,
    " Cash Flow to Liability": 0.34,
    " Total assets to GNP price": 0.29,
    " Net Income to Stockholder's Equity": 0.26,
    " Degree of Financial Leverage (DFL)": 0.24,
    " Interest Coverage Ratio (Interest expense to EBIT)": 0.17
}
'''
