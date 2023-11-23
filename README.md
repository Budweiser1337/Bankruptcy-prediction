# <p align="center"> Taiwanese Companies Bankruptcy Prediction Project</p>

- # Overview

Welcome to the Taiwanese Companies Bankruptcy Prediction project ! 

This project aims to develop a predictive model to identify the likelihood of bankruptcy for Taiwanese companies. 

In a work setting and by leveraging machine learning techniques and financial data, the goal would be to assist stakeholders, such as investors, creditors, and regulatory bodies, in making informed decisions.

- # Problem Explanation
As bankruptcy due to business failure can negatively affect the enterprise as well as the global economy, it is crucial to understand and predict whether a company is showing symptoms of going bankrupt or not. The idea is to analyse the distresses in the corporate by taking into considerations different KPI’s of the company. These distresses often lead to bankruptcy of the company if not alerted at the right time. The problem statement is to develop a prediction model which will predict whether a company can go bankrupt or not. This will help the company to take appropriate decisions.


- # Data Description
There are total 6819 samples in dataset and 96 features (including class label). 
Out of 6819, 6599 are negative (not bankrupt) and only 220 are positive (bankrupt).

Bankrupt?: Class label (target feature)

ROA(C) before interest and depreciation before interest: Return On Total Assets(C)

ROA(A) before interest and % after tax: Return On Total Assets(A)

ROA(B) before interest and depreciation after tax: Return On Total Assets(B)

Operating Gross Margin: Gross Profit/Net Sales

Realized Sales Gross Margin: Realized Gross Profit/Net Sales

Operating Profit Rate: Operating Income/Net Sales

Pre-tax net Interest Rate: Pre-Tax Income/Net Sales

After-tax net Interest Rate: Net Income/Net Sales

Non-industry income and expenditure/revenue: Net Non-operating Income Ratio

Continuous interest rate (after tax): Net Income-Exclude Disposal Gain or Loss/Net Sales

Operating Expense Rate: Operating Expenses/Net Sales

Research and development expense rate: (Research and Development Expenses)/Net Sales

Cash flow rate: Cash Flow from Operating/Current Liabilities

Interest-bearing debt interest rate: Interest-bearing Debt/Equity

Tax rate (A): Effective Tax Rate

Net Value Per Share (B): Book Value Per Share(B)

Net Value Per Share (A): Book Value Per Share(A)

XNet Value Per Share (C): Book Value Per Share(C)

Persistent EPS in the Last Four Seasons: EPS-Net Income

Cash Flow Per Share

Revenue Per Share (Yuan ¥): Sales Per Share

Operating Profit Per Share (Yuan ¥): Operating Income Per Share

Per Share Net profit before tax (Yuan ¥): Pretax Income Per Share

Realized Sales Gross Profit Growth Rate

Operating Profit Growth Rate: Operating Income Growth

After-tax Net Profit Growth Rate: Net Income Growth

Regular Net Profit Growth Rate: Continuing Operating Income after Tax Growth

Continuous Net Profit Growth Rate: Net Income-Excluding Disposal Gain or Loss Growth

Total Asset Growth Rate: Total Asset Growth

Net Value Growth Rate: Total Equity Growth

Total Asset Return Growth Rate Ratio: Return on Total Asset Growth

Cash Reinvestment %: Cash Reinvestment Ratio

Current Ratio

Quick Ratio: Acid Test

Interest Expense Ratio: Interest Expenses/Total Revenue

Total debt/Total net worth: Total Liability/Equity Ratio

Debt ratio %: Liability/Total Assets

Net worth/Assets: Equity/Total Assets

Long-term fund suitability ratio (A): (Long-term Liability+Equity)/Fixed Assets

Borrowing dependency: Cost of Interest-bearing Debt

Contingent liabilities/Net worth: Contingent Liability/Equity

Operating profit/Paid-in capital: Operating Income/Capital

Net profit before tax/Paid-in capital: Pretax Income/Capital

Inventory and accounts receivable/Net value: (Inventory+Accounts Receivables)/Equity

Total Asset Turnover

Accounts Receivable Turnover

Average Collection Days: Days Receivable Outstanding

Inventory Turnover Rate (times)

Fixed Assets Turnover Frequency

Net Worth Turnover Rate (times): Equity Turnover

Revenue per person: Sales Per Employee

Operating profit per person: Operation Income Per Employee

Allocation rate per person: Fixed Assets Per Employee

Working Capital to Total Assets

Quick Assets/Total Assets

Current Assets/Total Assets

Cash/Total Assets

Quick Assets/Current Liability

Cash/Current Liability

Current Liability to Assets

Operating Funds to Liability

Inventory/Working Capital

Inventory/Current Liability

Current Liabilities/Liability

Working Capital/Equity

Current Liabilities/Equity

Long-term Liability to Current Assets

Retained Earnings to Total Assets

Total income/Total expense

Total expense/Assets

Current Asset Turnover Rate: Current Assets to Sales

Quick Asset Turnover Rate: Quick Assets to Sales

Working capitcal Turnover Rate: Working Capital to Sales

Cash Turnover Rate: Cash to Sales

Cash Flow to Sales

Fixed Assets to Assets

Current Liability to Liability

Current Liability to Equity

Equity to Long-term Liability

Cash Flow to Total Assets

Cash Flow to Liability

CFO to Assets

Cash Flow to Equity

Current Liability to Current Assets

Liability-Assets Flag: 1 if Total Liability exceeds Total Assets, 0 otherwise

Net Income to Total Assets

Total assets to GNP price

No-credit Interval

Gross Profit to Sales

Net Income to Stockholder's Equity

Liability to Equity

Degree of Financial Leverage (DFL)

Interest Coverage Ratio (Interest expense to EBIT)

Net Income Flag: 1 if Net Income is Negative for the last two years, 0 otherwise

Equity to Liability
