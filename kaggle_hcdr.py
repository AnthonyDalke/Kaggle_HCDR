# Import necessary libraries and set global options

import pandas as pd
import numpy as np
import os
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, auc, balanced_accuracy_score, classification_report, confusion_matrix, roc_curve
from sklearn.impute import SimpleImputer
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

# Create list of columns with null values

train_null = app_train.columns[app_train.isna().any()].tolist()

print('Total count of columns in app_train: ' 
    + str(len(app_train.columns)))
print('Count of app_train columns with null values: ' 
    + str(len(train_null)))

# Distinguish columns to impute with medians from those to fill with 0

train_impute = [
    'EXT_SOURCE_1'
    , 'EXT_SOURCE_2'
    , 'EXT_SOURCE_3'
]
app_train[train_impute].describe()
train_zero = [x for x in train_null if x not in train_impute]

# Fill in null values

app_train[train_zero] = app_train[train_zero].fillna(0)
imp_base = SimpleImputer(
    missing_values=np.nan
    , strategy='median'
    )
imp_base.fit(app_train[train_impute])
test = imp_base.transform(app_train[train_impute])
app_train[train_impute] = imp_base.transform(app_train[train_impute])

# Fit XGBoost model on app_train with nulls

target = app_train['TARGET']
app_train.drop(
    columns=['TARGET']
    , inplace = True
    )

x_base, y_base = app_train, target
xtrain_base, ytrain_base, xtest_base, ytest_base = train_test_split(
    x_base
    , y_base
    , test_size=0.2
    , random_state=32
)

xgb_base = XGBClassifier(
    booster='gbtree'
    , objective='binary:logistic'
    , random_state=32
)
model_base = xgb_base.fit(xtrain_base, ytrain_base)

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