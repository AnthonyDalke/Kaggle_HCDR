# Import necessary libraries

import pandas as pd
import numpy as np
import os
pd.set_option('max_columns', None)

# Import files

os.chdir('/Users/anthony/Documents/Github/Kaggle_HCDR')

file_dict = {
    'app_test': 'application_test.csv'
    , 'app_train': 'application_train.csv'
    , 'bureau_bal': 'bureau_balance.csv'
    , 'bureau_hist': 'bureau.csv'
    , 'cc_bal': 'credit_card_balance.csv'
    , 'cc_payments': 'installments_payments.csv'
    , 'pos_hist': 'POS_CASH_balance.csv'
    , 'app_hist': 'previous_application.csv'
}

file_dfs = {idx: pd.read_csv(f) for idx, f in file_dict.items()}

# Write function to standardize EDA

def eda(df_name):
    print(df_name.head)
    print(df_name.describe())

# Explore app_train df

app_train = file_dfs['app_train']
eda(app_train)

# Explore bureau_bal df

bureau_bal = file_dfs['bureau_bal']
eda(bureau_bal)

# Explore bureau_hist df

bureau_hist = file_dfs['bureau_hist']
eda(bureau_hist)

# Explore cc_bal df

cc_bal = file_dfs['cc_bal']
eda(cc_bal)