import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE, BorderlineSMOTE, ADASYN
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import export_graphviz
from six import StringIO
import pydotplus
from sklearn.metrics import classification_report

app_df = pd.read_csv('https://drive.google.com/uc?id=1gjfTNwapOwg80NlUUkaW4bM9ffqLdtLk')
cr_df = pd.read_csv('https://drive.google.com/uc?id=1tF78o9Qcfc9IScQF1uxMAc3bS9c7SLbN')
#print(app_df.head())
#print(cr_df.shape)
#print(cr_df.head())

'''Preparing the Target Variable:

For customers having due for multiple months, the maximum number of months due is taken
Any ID with greater than equal to 1 months due is marked as Class 1 '''

print(cr_df['MONTHS_BALANCE'].value_counts())
cr_df = cr_df.sort_values(['ID','MONTHS_BALANCE'], ascending=False)
cr_df = cr_df.groupby('ID').agg(max).reset_index()

'''Status: 0: 1-29 days past due 1: 30-59 days past due 2: 60-89 days overdue 3: 90-119 days
 overdue 4: 120-149 days overdue 5: Overdue or bad debts, write-offs for more than 150 days C: paid off that month X: No loan for the month'''

#cr_df['STATUS'].value_counts()