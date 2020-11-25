import numpy as np  # for handling multi-dimensional array operation
import pandas as pd  # for reading data from csv 
import statsmodels.api as sm  # for finding the p-value
from sklearn.preprocessing import MinMaxScaler  # for normalization
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score 
from sklearn.utils import shuffle
# >> FEATURE SELECTION << #
def remove_correlated_features(X):
 def remove_less_significant_features(X, Y):
# >> MODEL TRAINING << #
  def compute_cost(W, X, Y):
   def calculate_cost_gradient(W, X_batch, Y_batch):
    def sgd(features, outputs):
     def init() :
          data = pd.read_csv('./data.csv')