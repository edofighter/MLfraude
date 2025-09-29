# librerías
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.train import train_model

#Testea que el modelo entrenado tenga el método predict y pueda hacer una predicción.
def test_train_model():
    X = np.random.rand(50, 5)
    y = np.random.randint(0, 2, 50)
    model = train_model(X, y)
    assert hasattr(model, "predict")
    # Prueba una predicción
    preds = model.predict(X[:5])
    assert len(preds) == 5
