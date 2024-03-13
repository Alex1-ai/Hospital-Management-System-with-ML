import pytest
from sitehandler.models import Doctor
from django.core.exceptions import ValidationError
from datetime import date

DOCTOR_ATTRIBUTE = {
    "name":'John Doe',
    'email':'john@example.com',
    "password":'password123',
    "gender":'Male',
    "phonenumber":'1234567890',
    "address":'123 Main St, City',
    "birthdate":date(1980, 1, 1),
    "bloodgroup":'AB+',
    'specialization':'Cardiology'
}

@pytest.mark.django_db
def test_doctor_creation():
    doctor = Doctor.objects.create(
        **DOCTOR_ATTRIBUTE
    )
    assert doctor.name == DOCTOR_ATTRIBUTE['name']
    assert doctor.email == DOCTOR_ATTRIBUTE['email']
    assert doctor.gender == DOCTOR_ATTRIBUTE['gender']
    assert doctor.phonenumber == DOCTOR_ATTRIBUTE['phonenumber']
    assert doctor.address == DOCTOR_ATTRIBUTE['address']
    assert doctor.birthdate == DOCTOR_ATTRIBUTE['birthdate']
    assert doctor.bloodgroup == DOCTOR_ATTRIBUTE['bloodgroup']
    assert doctor.specialization == DOCTOR_ATTRIBUTE['specialization']

@pytest.mark.django_db
def test_doctor_str_representation():
    doctor = Doctor.objects.create(
        **DOCTOR_ATTRIBUTE
    )
    assert str(doctor) == 'John Doe'