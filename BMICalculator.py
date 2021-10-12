import os
import json
import pandas as pd
from IPython.display import display, HTML





def bmi_calculator(gwh_data=None):
    """
    Function to calculate the BMI,
    determine the BMI Category and
    Health risk
    
    Keyword arguments:
    :gwh_data: Dictionary containing
               Gender, Height, Weight
               (Default -> None)
    Return          
    :return: Updated/Calculated values
             i.e BMI, BMI Category and
             Health risk.
    """
    
    GENDER = gwh_data["Gender"]
    HEIGHT = gwh_data["Height"] / 100
    WEIGHT = gwh_data["Weight"]
    
    
    BMI = round(WEIGHT/(HEIGHT*HEIGHT),1)
    
    
    if BMI <= 18.4:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Underweight",
        "Health risk":"Malnutrition risk"})
        
    elif 18.5 <= BMI <= 24.9:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Normal weight",
        "Health risk":"Low risk"})
    
    elif 25 <= BMI <= 29.9:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Overweight",
        "Health risk":"Enhanced risk"})
        
    elif 30 <= BMI <= 34.9:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Moderately obese",
        "Health risk":"Medium risk"})
    
    elif 35 <= BMI <= 39.9:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Severely obese",
        "Health risk":"High risk"})
    
    elif BMI >= 40:
        gwh_data.update({"BMI":BMI,
        "BMI Category":"Very severely obese",
        "Health risk":"Very high risk"})
        
    return gwh_data


if __name__ == "__main__":
    

    # json_file = os.environ.get('JSON_FILE')
    JSON_FILE="gender-weight-height.json"
    # Read the json file and load the data into json object
    with open(JSON_FILE,"r") as gwh:
        gwh_data = json.load(gwh)
   


    bmi_results = []

    # Calculating BMI for each record and appending result to list
    for data in gwh_data:
        bmi_results.append(bmi_calculator(data))

    # Creating pandas datafrmae form the resultant list of results
    df = pd.DataFrame(bmi_results)
    numbr_overweight = df["BMI Category"].eq("Overweight").sum()

    # Printing result 
    print(df)  
    print("Number of overweight people: {}".format(numbr_overweight))

    # Saving the result in as html
    df.to_html("table.html")
    
