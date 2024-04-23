# Bu kod hücresi ml.py dosyasında bulunmalıdır.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import LSTM, Dense



def read_data(data):
  """ Reads the data as a Pandas DataFrame. """
  df = pd.read_csv(data, nrows=600)
  # df.columns = Index(['Datetime', 'AEP_MW'], dtype='object')
  df['Datetime'] = pd.to_datetime(df['Datetime'])
  df.set_index('Datetime', inplace=True)
  return df

def initial_tests(data):
  """ Runs initial tests on the data. """
  result = adfuller(data[data.columns[0]])
  print('ADF Statistic:', result[0])
  print('p-value:', result[1])
  print('Critical Values:', result[4])

  if result[1] < 0.05 and result[0] < result[4]['5%']:
        print("Veri durağan.")
  else:
        print("Veri durağan değil.")


def main():
  """ Driver function. """
  df = read_data('AEP_hourly_mini.csv')
  initial_tests(df)


main()
