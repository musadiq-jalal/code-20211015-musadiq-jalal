import pytest
from .BMICalculator import bmi_calculator


def test_bmi_calculator_results():
     result = bmi_calculator({'Gender': "Male", 'Height': 173,'Weight': 69.1})      
     assert result == {'Gender': 'Male', 'Height': 173,'Weight': 69.1, 
                            'BMI': 23.1, 'BMI Category': 'Normal weight', 
                            'Health risk': 'Low risk'}

def test_bmi_calculator_weight():
     result = bmi_calculator({'Gender': "Female", 'Height': 160, 'Weight': 69.1}) 
     assert result.get("Weight") == 69.1

def test_bmi_calculator_category():
    result = bmi_calculator({'Gender': "Male", 'Height': 165, 'Weight': 91.1}) 
    assert result.get("BMI Category") == "Moderately obese"

def test_bmi_calculator_bmi():
   result = bmi_calculator({'Gender': "Male", 'Height': 173,'Weight': 119.1})
   assert isinstance(result["BMI"],float) 
# 
