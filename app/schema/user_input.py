from pydantic import BaseModel, Field, field_validator, computed_field
from typing import Optional, Annotated, Literal
from core.config import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    age: Annotated[int, Field(ge=0, le=120)] = Field(..., description="Age of the user, must be between 0 and 120")
    weight: Annotated[float, Field(ge=0.0)] = Field(..., description="Weight of the user in kilograms, must be non-negative")
    height: Annotated[float, Field(ge=0.0)] = Field(..., description="Height of the user in centimeters, must be non-negative")
    income_lpa: Optional[Annotated[float, Field(ge=0.0)]] = Field(..., description="Annual income of the user in lakhs per annum, must be non-negative")
    smokes: Annotated[bool, Field(description="Indicates if the user smokes")]
    city: Annotated[str, Field(description="City of residence of the user")]
    occupation: Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'] = Field(..., description="Occupation of the user, must be one of the specified values")
    
    @field_validator('city')
    @classmethod
    def validate_city(cls, v: str) -> str:
        return v.strip().title()
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smokes and self.bmi > 30:
            return "high"
        elif self.smokes or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 18:
            return "minor"
        elif self.age < 60:
            return "adult"
        else:
            return "senior"
        
    @computed_field
    @property
    def city_tier(self) -> str:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3