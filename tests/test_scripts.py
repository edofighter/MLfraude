# librerías
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from src.data_prep import split_data
from src.features import scale_features
from sklearn.preprocessing import StandardScaler

#Testea que split_data divide correctamente los datos.
def test_split_data():
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    X_train, X_test, y_train, y_test = split_data(X, y)
    assert len(X_train) > 0 and len(X_test) > 0
    assert len(y_train) > 0 and len(y_test) > 0

#Testea que scale_features escala correctamente los datos.
def test_scale_features():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    X_train_scaled, X_test_scaled, scaler = scale_features(df, df)
    assert X_train_scaled.shape == df.shape
    assert X_test_scaled.shape == df.shape
    assert isinstance(scaler, StandardScaler)

