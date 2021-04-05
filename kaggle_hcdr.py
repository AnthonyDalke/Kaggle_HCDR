# Import necessary libraries

import pandas as pd
import numpy as np
import os

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