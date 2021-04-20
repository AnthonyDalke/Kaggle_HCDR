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

# Confirm app_test has same columns as app_train

app_test = file_dfs['app_test']

train_col = sorted(app_train.columns.tolist())
len(train_col)
test_col = sorted(app_test.columns.tolist())
len(test_col)
set(train_col) - set(test_col)
train_col.remove('TARGET')
len(train_col)

match_col = 0 
mismatch_col = []
for i in range(0, len(test_col)):
    if test_col[i] == train_col[i]:
        match_col += 1
    else:
        mismatch_col.append(test_col[i])
if match_col == len(test_col):
    print('Columns match!')
else:
    print('These columns do not match:')
    print(mismatch_col)

# Verify SK_ID_CURR in app_test exist in bureau_hist and app_hist

print('Total count of unique SK_ID_CURR in test set: ' 
    + str(len(app_test['SK_ID_CURR'].unique()))
    )
print('SK_ID_CURR in test set and bureau_hist: ' 
    + str(len(app_test['SK_ID_CURR'][(app_test['SK_ID_CURR'].isin(bureau_hist['SK_ID_CURR']))].unique()))
    )
print('SK_ID_CURR in test set but not bureau_hist: ' 
    + str(len(app_test['SK_ID_CURR'][~(app_test['SK_ID_CURR'].isin(bureau_hist['SK_ID_CURR']))].unique()))
    )
print(
    'Ratio of SK_ID_CURR in test set but not bureau_hist: ' 
    + str("{:.2f}".format(len(app_test['SK_ID_CURR'][~(app_test['SK_ID_CURR'].isin(bureau_hist['SK_ID_CURR']))].unique())
     / len(app_test['SK_ID_CURR'].unique()))
     )
    )

print('SK_ID_CURR in test set and app_hist: ' 
    + str(len(app_test['SK_ID_CURR'][(app_test['SK_ID_CURR'].isin(app_hist['SK_ID_CURR']))].unique()))
    )
print('SK_ID_CURR in test set but not app_hist: ' 
    + str(len(app_test['SK_ID_CURR'][~(app_test['SK_ID_CURR'].isin(app_hist['SK_ID_CURR']))].unique()))
    )
print(
    'Ratio of SK_ID_CURR in test set but not app_hist: ' 
    + str("{:.2f}".format(len(app_test['SK_ID_CURR'][~(app_test['SK_ID_CURR'].isin(app_hist['SK_ID_CURR']))].unique())
     / len(app_test['SK_ID_CURR'].unique()))
     )
    )

# Explore bureau_bal df

bureau_bal = file_dfs['bureau_bal']
eda(bureau_bal)

# Explore bureau_hist df

bureau_hist = file_dfs['bureau_hist']
eda(bureau_hist)

# Explore cc_bal df

cc_bal = file_dfs['cc_bal']
eda(cc_bal)

# Explore cc_payments df

cc_payments = file_dfs['cc_payments']
eda(cc_payments)

# Explore pos_hist df

pos_hist = file_dfs['pos_hist']
eda(pos_hist)

# Explore app_hist df

app_hist = file_dfs['app_hist']
eda(app_hist)