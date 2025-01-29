# Diabetes-Vorhersage mit Machine Learning
Dieses Projekt sagt anhand verschiedener Gesundheitskennzahlen voraus, ob ein Patient an Diabetes leidet. Das verwendete Datensatz ist die [Diabetes-Datenbank](https://www.kaggle.com/datasets/johndasilva/diabetes?select=diabetes.csv) von Kaggle. Der Hauptklassifikationsalgorithmus ist ein Random-Forest, zusätzlich werden Vergleiche mit anderen Modellen wie logistische Regression, Entscheidungsbäume und Support Vector Machine (SVM) durchgeführt.

## Projektübersicht
Das Ziel dieses Projekts ist es, einen reibungslosen Prozess zur Vorhersage von Diabetes zu schaffen. Dies wird durch die Erstellung eines Machine-Learning-Modells erreicht, das Gesundheitsparameter analysiert. Die Webanwendung ermöglicht die Eingabe von Benutzerdaten, verarbeitet diese mithilfe des Modells und zeigt das Vorhersageergebnis an. Die Eingabedaten die vom Benutzer erwartet werden lauten:
- Anzahl der Schwangerschaften
- Glukose Level
- Blutdruck
- Hautdicke in mm
- Insulin Level
- Body-Mass-Index (BMI)
- Diabetes-Stammfunktion (DPF)
- Alter

Ausgabe: Diabetes Positiv oder Diabetes Negativ.

## Technische Aspekte
### 🖥 <ins>Frontend</ins>
<div align="left">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5-Logo">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS-Logo">
</div>

### ⚙️<ins>Backend</ins>
<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python-Logo">
  <img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask-Logo">
</div>

### 📈<ins>Datenanalyse und Vorhersage</ins>
<div align="left">
  <img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas-Logo">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn-Logo">
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy-Logo">
</div>

### 📉 <ins>Datenvisualisierung</ins>
<div align="left">
  <img src="https://img.shields.io/badge/Matplotlib-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Seaborn-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white">
</div>

## Projektstruktur
```
.
├── data
│   ├── diabetes.csv           # Datensatz
├── models
│   ├── random_forest.pkl      # Gespeichertes Random-Forest-Modell
├── static
│   ├── styles.css             # CSS-Styles für die HTML-Vorlage
├── templates
│   ├── index.html             # HTML-Vorlage für die Flask-Web-App
├── app.py                     # Flask-Anwendung für die Webschnittstelle
├── diabetes_predict.ipynb     # Jupyter Notebook für die Datenanalyse, Visualisierung 
├── model.py                   # Python-Skript für das Training und Speichern des Modells
├── requirements.txt           # Liste der Projektabhängigkeiten
```

## Installation
1. Repository klonen:
   ```bash
   git clone https://github.com/yzcodeX/diabetes-prediction.git
   cd diabetes-prediction
   ```
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. Starten der Flask-App:
   ```bash
    python app.py
   ```
4. Browser öffnen und Anwendung unter `http://localhost:5000` oder `http://127.0.0.1:5000/` aufrufen. Anschließend Eingabedaten in das Formular eingeben, um eine Vorhersage zu erhalten.

## Lizenz
Dieses Projekt ist unter der  <a href="https://github.com/yzcodeX/diabetes-prediction/blob/main/LICENSE"> MIT-Lizenz</a> lizenziert.


