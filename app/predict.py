import pickle
import pandas as pd

with open('../models/model.pkl', 'rb') as file:
    model = pickle.load(file)

MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()

def predict_output(user_input: dict) -> dict:
    """
    Predict the health insurance category based on user input.

    Args:
        user_input (dict): User input data.

    Returns:
        dict: Prediction response containing predicted category, confidence, and class probabilities.
    """
    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = round(max(probabilities), 4)
    class_probabilities = {label: round(prob, 4) for label, prob in zip(class_labels, probabilities)}

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "class_probabilities": class_probabilities
    }
