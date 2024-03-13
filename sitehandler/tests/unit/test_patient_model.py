# tests/unit/test_models.py
import pytest
from sitehandler.models import Patient
from datetime import date

# Common attributes
COMMON_ATTRIBUTES = {
    'name': 'Alice Smith',
    'email': 'alice@example.com',
    'password': 'password123',
    'gender': 'Female',
    'phonenumber': '9876543210',
    'address': '456 Elm St, Town',
    'birthdate': date(1990, 5, 15),
    'bloodgroup': 'O+',
}

@pytest.mark.django_db
def test_patient_creation():
    patient = Patient.objects.create(**COMMON_ATTRIBUTES)
    assert patient.name == 'Alice Smith'
    assert patient.email == 'alice@example.com'
    assert patient.gender == 'Female'
    assert patient.phonenumber == '9876543210'
    assert patient.address == '456 Elm St, Town'
    assert patient.birthdate == date(1990, 5, 15)
    assert patient.bloodgroup == 'O+'

@pytest.mark.django_db
def test_patient_str_representation():
    patient = Patient.objects.create(**COMMON_ATTRIBUTES)
    assert str(patient) == 'Alice Smith'
