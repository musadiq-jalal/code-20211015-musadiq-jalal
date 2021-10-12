import pytest
from .BMICalculator import bmi_calculator


def test_bmi_calculator():
    assert bmi_calculator(
        {'Gender': "Male", 
         'Height': 173, 
         'Weight': 69.1}) == {'Gender': 'Male', 'Height': 173,'Weight': 69.1, 
                            'BMI': 23.1, 'BMI Category': 'Normal weight', 
                            'Health risk': 'Low risk'}

    assert bmi_calculator(
         {'Gender': "Female", 
                'Height': 160, 
                'Weight': 69.1}) == {'Gender': 'Female','Height': 160, 'Weight': 69.1, 
                                'BMI': 27.0, 'BMI Category': 'Overweight',
                                'Health risk': 'Enhanced risk'}
    assert bmi_calculator(
         {'Gender': "Male", 
          'Height': 165, 
          'Weight': 91.1}) == {'Gender': 'Male','Height': 165,'Weight': 91.1,
                                 'BMI': 33.5,'BMI Category': 'Moderately obese',
                                 'Health risk': 'Medium risk'}
    assert bmi_calculator(
         {'Gender': "Male", 
          'Height': 173, 
        'Weight': 119.1}) == {'Gender': 'Male', 'Height': 173, 'Weight': 119.1,
                                    'BMI': 39.8,'BMI Category': 'Severely obese',
                                    'Health risk': 'High risk'}
