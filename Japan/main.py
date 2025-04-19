import pandas as pd
from os import listdir
from os.path import isfile, join
import tqdm
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.preprocessing import OneHotEncoder
import sklearn
import gc
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from copy import deepcopy
from sklearn.metrics import r2_score
import itertools
import matplotlib.pyplot as plt
import os