#librerias
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

#Evalúa el modelo con métricas clave.
#Retorna un diccionario con classification_report, roc_auc y confusion_matrix.
def evaluate_model(model, X_test, y_test):
    # Predicciones
    y_pred = model.predict(X_test)
    # Manejo si el modelo no tiene predict_proba
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_prob)
    else:
        y_prob = None
        auc = None

    report = classification_report(y_test, y_pred, digits=4)
    cm = confusion_matrix(y_test, y_pred)
    return {'report': report, 'roc_auc': auc, 'confusion_matrix': cm}


