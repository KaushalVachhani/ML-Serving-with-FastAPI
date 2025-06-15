from fastapi import FastAPI
from fastapi.responses import JSONResponse
from predict import model, MODEL_VERSION, predict_output
from schema.prediction_response import PredictionResponse
from schema.user_input import UserInput

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Health Insurance API"}

@app.get("/health")
def health_check():
    return {"status": "healthy",
            "version": MODEL_VERSION,
            "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict(user_input: UserInput):
    """
    Predict the health insurance category based on user input.

    Args:
        user_input (UserInput): User input data.

    Returns:
        PredictionResponse: Prediction response containing predicted category, confidence, and class probabilities.
    """
    try:
        prediction = predict_output(user_input.dict())
        return JSONResponse(content={"response": prediction}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)