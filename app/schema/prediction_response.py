from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(..., description="Predicted category of the user based on input data", example="High")
    confidence: float = Field(..., description="Confidence level of the prediction", example=0.85)
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities of each class in the prediction", example={"High": 0.85, "Medium": 0.10, "Low": 0.05})