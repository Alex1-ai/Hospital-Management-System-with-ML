# tests/unit/test_models.py
import pytest
from sitehandler.models import Diabetes_Prediction, Patient
from django.core.validators import MinValueValidator, MaxValueValidator

# Common attributes
COMMON_ATTRIBUTES = {
    'patient': None,  # Patient instance will be assigned later
    'pregnancies': 3,
    'glucose': 100,
    'blood_pressure': 70,
    'skin_thickness': 30,
    'insulin': 50,
    'bmi': 25.5,
    'diabetes_pedigree_func': 0.4,
    'age': 35,
    'outcome': 0,
}

@pytest.mark.django_db
def test_diabetes_prediction_creation():
    # Create a patient
    patient = Patient.objects.create(
        name='Alice Smith',
        email='alice@example.com',
        password='password123',
        gender='Female',
        phonenumber='9876543210',
        address='456 Elm St, Town',
        birthdate='1990-05-15',
        bloodgroup='O+'
    )
    
    # Update patient field in COMMON_ATTRIBUTES
    COMMON_ATTRIBUTES['patient'] = patient
    
    # Create Diabetes_Prediction instance
    diabetes_prediction = Diabetes_Prediction.objects.create(**COMMON_ATTRIBUTES)
    
    # Assertion
    assert diabetes_prediction.patient == patient
    assert diabetes_prediction.pregnancies == 3
    assert diabetes_prediction.glucose == 100
    assert diabetes_prediction.blood_pressure == 70
    assert diabetes_prediction.skin_thickness == 30
    assert diabetes_prediction.insulin == 50
    assert diabetes_prediction.bmi == 25.5
    assert diabetes_prediction.diabetes_pedigree_func == 0.4
    assert diabetes_prediction.age == 35
    assert diabetes_prediction.outcome == 0
