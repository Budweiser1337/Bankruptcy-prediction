# <p align="center"> Taiwanese Companies Bankruptcy Prediction Project</p>

- # Overview

  Welcome to the Taiwanese Companies Bankruptcy Prediction project ! 

  This project aims to develop a predictive model to identify the likelihood of bankruptcy for Taiwanese companies. 

  In a work setting and by leveraging machine learning techniques and financial data, the goal would be to assist stakeholders, such as investors, creditors, and regulatory bodies in making informed decisions.

- # Problem Explanation
  As bankruptcy due to business failure can negatively affect the enterprise as well as the global economy, it is crucial to understand and predict whether a company is showing symptoms of going bankrupt or not.   The idea is to analyse the distresses in the corporate by taking into considerations different KPI’s of the company. These distresses often lead to bankruptcy of the company if not alerted at the right time.     The problem statement is to develop a prediction model which will predict whether a company can go bankrupt or not. This will help the company take appropriate decisions.


- # Data Description
  There is a total of 6819 samples in the dataset with 96 features (including the class label). 
  Out of the 6819 samples, 6599 are negative (not bankrupt) and only 220 are positive (bankrupt).
  You will find at the end of the README the list of all features in the dataset.

- # Exploratory Data Analysis
  Visualizations of class distributions, histograms and scatterpoints of relevant features to provide good insights into the data.
  Visualizations of feature importance for different models.

- # Data Preprocessing
1. Data cleaning
   We checked for missing and duplicated values, there was none. However we did identify and address zero values in certain columns by imputing the mean.
   
3. Feature engineering and feature selection
   Removal of highly correlated features to improve model interpretability and reduce multicollinearity.
   Experimented with both Recursive Feature Elimination (RFE) and Principal Component Analysis (PCA) for feature selection.
   
4. Solving the class imbalance problem
   Applied oversampling techniques (SMOTE and RandomOverSampler).

- # Model Training and Evaluations
1. Model selection
   Experimented with GradientBoosting, RandomForest, and MLPClassifier.
   
3. Grid Search and cross-validation
   Used Grid Search to find optimal hyperparameters.
   Used cross-validation to ensure that the model performance metrics are robust and not heavily dependent on a specific train-test split.
   
5. Evaluation metrics and visualization
   We used a variety of metrics including f1_score, precision, recall, PR AUC, ROC AUC for evaluation as the accuracy isn't very representative of the model's performance for this kind of problem.
   Visualized how the models performed on the test dataset on a confusion matrix.

- # Conclusion

  The best model overall was the MLP Classifier with 0.77 ROC and 0.62 recall after performing Recursive Feature Elimination and oversampling the data using SMOTE, however, it wasn't the best accross all metrics   as the precision (0.22) and f1 score (0.32) were lower compared to the other models.
  
  Computational costs were heavily reduced whether it was by reducing the number of features with PCA or RFE.
  
  The GridSearchCV was faster by 50% on average for all 3 models we experimented with.

  We observed that companies which had high "Interest-bearing debt interest rate", "Persistent EPS in the Last Four Seasons", "Total debt/Total net worth", "Equity to Liability" and "Debt Ratio %" tended to end up bankrupt more often as these features  were selected by RFE regardless of the model.

- # Future Work

  For future research on this subject it might be interesting to explore other imputation methods like median or machine learning-based imputation techniques and consider trying different ratios of oversampling and evaluating their impact on model performance. Here we limited our project to 3 models but training other models such as Support Vector Machines (SVM) or K-Nearest Neighbors (KNN) might show good performance.

- # List of features

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

Cash Flow Per Share: Earnings generated as cash flow per share

Revenue Per Share (Yuan ¥): Sales Per Share

Operating Profit Per Share (Yuan ¥): Operating Income Per Share

Per Share Net profit before tax (Yuan ¥): Pretax Income Per Share

Realized Sales Gross Profit Growth Rate: Percentage change in the growth rate of realized gross profit

Operating Profit Growth Rate: Operating Income Growth

After-tax Net Profit Growth Rate: Net Income Growth

Regular Net Profit Growth Rate: Continuing Operating Income after Tax Growth

Continuous Net Profit Growth Rate: Net Income-Excluding Disposal Gain or Loss Growth

Total Asset Growth Rate: Total Asset Growth

Net Value Growth Rate: Total Equity Growth

Total Asset Return Growth Rate Ratio: Return on Total Asset Growth

Cash Reinvestment %: Cash Reinvestment Ratio

Current Ratio: Ratio of current assets to current liabilities

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

Total Asset Turnover: Efficiency in using total assets to generate sales

Accounts Receivable Turnover: Frequency of converting accounts receivable to cash

Average Collection Days: Days Receivable Outstanding

Inventory Turnover Rate (times): Rate of inventory turnover within a given period

Fixed Assets Turnover Frequency: Frequency of utilizing fixed assets for generating sales

Net Worth Turnover Rate (times): Equity Turnover

Revenue per person: Sales Per Employee

Operating profit per person: Operation Income Per Employee

Allocation rate per person: Fixed Assets Per Employee

Working Capital to Total Assets: Proportion of working capital to total assets

Quick Assets/Total Assets: Ratio of quick assets to total assets

Current Assets/Total Assets: Proportion of current assets to total assets

Cash/Total Assets: Ratio of cash to total assets

Quick Assets/Current Liability: Proportion of quick assets to current liabilities

Cash/Current Liability: Ratio of cash to current liabilities.

Current Liability to Assets: Proportion of current liabilities to total assets

Operating Funds to Liability: Ratio of operating funds to total liabilities

Inventory/Working Capital: Proportion of inventory to working capital

Inventory/Current Liability: Ratio of inventory to current liabilities

Current Liabilities/Liability: Proportion of current liabilities to total liabilities

Working Capital/Equity: Ratio of working capital to equity

Current Liabilities/Equity: Proportion of current liabilities to equity

Long-term Liability to Current Assets: Ratio of long-term liabilities to current assets

Retained Earnings to Total Assets: Ratio of retained earnings to total assets

Total income/Total expense: Proportion of total income to total expenses

Total expense/Assets: Ratio of total expenses to total assets

Current Asset Turnover Rate: Current Assets to Sales

Quick Asset Turnover Rate: Quick Assets to Sales

Working capitcal Turnover Rate: Working Capital to Sales

Cash Turnover Rate: Cash to Sales

Cash Flow to Sales: Proportion of cash flow to total sales

Fixed Assets to Assets: Proportion of fixed assets to total assets

Current Liability to Liability: Ratio of current liabilities to total liabilities

Current Liability to Equity: Proportion of current liabilities to equity

Equity to Long-term Liability: Ratio of equity to long-term liabilities

Cash Flow to Total Assets: Proportion of cash flow to total assets

Cash Flow to Liability: Ratio of cash flow to total liabilities

CFO to Assets: Ratio of CFO (Cash Flow from Operating) to total assets

Cash Flow to Equity: Proportion of cash flow to equity

Current Liability to Current Assets: Ratio of current liabilities to current assets

Liability-Assets Flag: 1 if Total Liability exceeds Total Assets, 0 otherwise

Net Income to Total Assets: Proportion of net income to total assets

Total assets to GNP price: Ratio of total assets to GNP price

No-credit Interval: Time interval without credit

Gross Profit to Sales: Ratio of gross profit to total sales

Net Income to Stockholder's Equity: Proportion of net income to stockholder's equity

Liability to Equity: Ratio of total liabilities to equity

Degree of Financial Leverage (DFL): Degree of financial risk associated with leverage

Interest Coverage Ratio (Interest expense to EBIT): Ratio of interest expenses to earnings before interest and taxes (EBIT)

Net Income Flag: 1 if Net Income is Negative for the last two years, 0 otherwise

Equity to Liability: Ratio of ownership interest to total liabilities
