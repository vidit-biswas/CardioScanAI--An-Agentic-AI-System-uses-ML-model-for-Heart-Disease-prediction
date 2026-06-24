import joblib
import pandas as pd

model = joblib.load("models/heart_model.pkl")
encoders = joblib.load("models/label_encoders.pkl")


def predict_heart_disease(data: dict):

    print("\nDATA RECEIVED:")
    print(data)
    print(type(data))

    df = pd.DataFrame([data])

    print("\nDATAFRAME:")
    print(df)
    print(df.columns)

    categorical_cols = [
        "Sex",
        "ChestPainType",
        "RestingECG",
        "ExerciseAngina",
        "ST_Slope"
    ]
    for col in categorical_cols:
        df[col] = encoders[col].transform(df[col])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "risk_score": round(float(probability) * 100, 2)
    }