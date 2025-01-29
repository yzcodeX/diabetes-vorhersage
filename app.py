import joblib
import os
import numpy               as np

from flask                 import Flask, request, render_template
from sklearn.preprocessing import StandardScaler


# Flask-App erstellen
app = Flask(__name__)

# Modell laden
MODEL_PATH = "models/random_forest.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    raise FileNotFoundError(f"Modell in {MODEL_PATH} nicht gefunden.")


# Startseite mit Eingabeformular
@app.route("/")
def index():
    return render_template("index.html", prediction_result = None)

# Vorhersage nachdem Button gedrückt wurde
@app.route("/predict", methods = ["POST"])
def predict():
    try:
         # Eingabedaten aus Formular abrufen
        input_data = [
            int(request.form["Pregnancies"]),
            float(request.form["Glucose"].replace(",", ".")),
            float(request.form["BloodPressure"].replace(",", ".")),
            float(request.form["SkinThickness"].replace(",", ".")),
            float(request.form["Insulin"].replace(",", ".")),
            float(request.form["BMI"].replace(",", ".")),
            float(request.form["DiabetesPedigreeFunction"].replace(",", ".")),
            int(request.form["Age"])
        ]
        
        # Skalieren der Input Daten
        sc = StandardScaler()
        input_data_scaled = sc.fit_transform([input_data])
        input_data_scaled = np.array(input_data).reshape(1, -1)
        
        # Vorhersage mit dem geladenen Modell durchführen
        prediction = model.predict(input_data_scaled)
        result     = "Diabetes Positiv." if prediction == 1 else "Diabetes Negativ."  
        
    except Exception as e:
        result = f"Fehler: {e}"

    return render_template("index.html", prediction_result = result)

# Zurücksetzen 
@app.route("/reset", methods=["POST"])
def reset():
    # Leite zurück zur Startseite
    return render_template("index.html", prediction_result = None)

if __name__ == "__main__":
    app.run(debug = True)
