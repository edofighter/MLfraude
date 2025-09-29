# Librerías
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

 #Carga los datos desde un archivo CSV.
def load_raw_data(file_path) -> pd.DataFrame:
    return pd.read_csv(file_path)

 #Divide los datos en conjuntos de entrenamiento y prueba.
def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

#Guarda los datasets procesados en formato .npy.
def save_numpy(X_train, X_test, y_train, y_test, output_dir='../data/processed/'):
    os.makedirs(output_dir, exist_ok=True)
    np.save(os.path.join(output_dir, 'X_train.npy'), X_train)
    np.save(os.path.join(output_dir, 'X_test.npy'), X_test)
    np.save(os.path.join(output_dir, 'y_train.npy'), y_train)
    np.save(os.path.join(output_dir, 'y_test.npy'), y_test)