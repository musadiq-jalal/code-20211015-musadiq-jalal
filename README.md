# BMICalculator
Calculates the BMI for each record in a json file containing: Gender (Male/Female), Height (cm) and Weight (kg) Generates the BMI Category and Health risk on the basis of the chart provided

## BMIClaculator.py
1: Read the json file and load the data into json object \n
2: Calculating BMI for each record and appending result to list\n
3: Creates pandas datafrmae form the resultant list of results\n
4: Prints the result and numbre of overweighted people.

## test_BMICalculator.py
Is the testing script for the BMICalculator

## deploy.sh
Runs the setup, test and script.

To run the calculator simply run the deploy.sh file on the root
```source deploy.sh```


## gender-weight-height.json
Is a dummy data file with 10,000 records.