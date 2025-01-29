import os 
import joblib
import pandas                as pd
import numpy                 as np

from sklearn.ensemble        import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Daten laden
DATA_PATH = "./data/diabetes.csv"
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Datei nicht in {DATA_PATH} gefunden.")

df = pd.read_csv(DATA_PATH)

# Ersetzen der 0-Werte von "Glucose", "BloodPressure", "SkinThickness", "Insulin" und "BMI" mit NaN
df_copy           = df.copy(deep = True)

features          = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
df_copy[features] = df_copy[features].replace(0, np.NaN)

# Ersetzen der NaN-Werte durch den Mittelwert/Median
df_copy['Glucose']       = df_copy['Glucose'].fillna(df_copy['Glucose'].mean())
df_copy['BloodPressure'] = df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean())
df_copy['SkinThickness'] = df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median())
df_copy['Insulin']       = df_copy['Insulin'].fillna(df_copy['Insulin'].median())
df_copy['BMI']           = df_copy['BMI'].fillna(df_copy['BMI'].median())


# Modell erstellen und trainieren
# Features und Zielvariable definieren
X = df.drop('Outcome', axis=1) # Alle Spalten außer "Outcome"
y = df['Outcome']              # Zielvariable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1)

# Random Forest Modell erstellen
rfc_model = RandomForestClassifier(n_estimators = 200, random_state = 1)
rfc_model.fit(X_train, y_train)

# # Modell speichern
MODEL_PATH = "./models/random_forest.pkl"
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok = True) # Ordner erstellen, falls nicht vorhanden
joblib.dump(rfc_model, MODEL_PATH)
print("Modell wurde erfolgreich gespeichert: ", MODEL_PATH)