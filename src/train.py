#librerias
import joblib
from sklearn.ensemble import RandomForestClassifier

#Entrena un modelo RandomForest y lo retorna.
def train_model(X_train, y_train):
    #Entrenamiento del modelo
    model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
    model.fit(X_train, y_train)
    return model

#Guarda el modelo entrenado en un archivo .pkl
def save_model(model, path='../models/fraud_model.pkl'):
    joblib.dump(model, path)