from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load saved components
model = load_model("dnn_attention_model.h5")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        df = pd.read_csv(file)

        if 'Label' in df.columns:
            df = df.drop('Label', axis=1)

        # Scale
        df_scaled = scaler.transform(df)

        # Predict all rows
        preds = model.predict(df_scaled)

        # Convert to labels
        class_indices = np.argmax(preds, axis=1)
        labels = label_encoder.inverse_transform(class_indices)

        # 🔥 COUNT each class
        from collections import Counter
        count = Counter(labels)

        # Get most common prediction
        final_label = count.most_common(1)[0][0]

        # Confidence = percentage of that class
        total = len(labels)
        confidence = (count[final_label] / total) * 100

        return render_template('result.html',
                               final_label=final_label,
                               confidence=round(confidence, 2))

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)