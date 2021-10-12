if [ ! -d "bmi_env/" ]; then
    virtualenv -p /usr/bin/python3 bmi_env
    source bmi_env/bin/activate
    pip install -r requirements.txt 
fi
source bmi_env/bin/activate
pytest
python BMICalculator.py