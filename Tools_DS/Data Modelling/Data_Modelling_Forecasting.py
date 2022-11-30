import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA

data = pd.read_excel(r"C:\Users\nanda\Downloads\owid-covid-data_real.xlsx")
#print(data.head(3))

