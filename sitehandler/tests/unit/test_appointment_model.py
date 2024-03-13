# tests/unit/test_models.py
import pytest
from sitehandler.models import Appointment
from datetime import date

# Common attributes
COMMON_ATTRIBUTES = {
    'doctorname': 'Dr. Smith',
    'doctoremail': 'smith@example.com',
    'patientname': 'Alice',
    'patientemail': 'alice@example.com',
    'appointmentdate': date(2024, 4, 1),
    'appointmenttime': '10:00',
    'symptoms': 'Fever and cough',
    'status': False,
    'prescription': 'Take plenty of rest and fluids',
}

@pytest.mark.django_db
def test_appointment_creation():
    appointment = Appointment.objects.create(**COMMON_ATTRIBUTES)
    assert appointment.doctorname == 'Dr. Smith'
    assert appointment.doctoremail == 'smith@example.com'
    assert appointment.patientname == 'Alice'
    assert appointment.patientemail == 'alice@example.com'
    assert appointment.appointmenttime == '10:00'
    assert appointment.appointmentdate == date(2024, 4, 1)
    assert appointment.symptoms == 'Fever and cough'
    assert appointment.status == False
    assert appointment.prescription == 'Take plenty of rest and fluids'
    # for key, value in COMMON_ATTRIBUTES.items():
    #     assert getattr(appointment, key) == value

@pytest.mark.django_db
def test_appointment_str_representation():
    appointment = Appointment.objects.create(**COMMON_ATTRIBUTES)
    assert str(appointment) == f"{COMMON_ATTRIBUTES['patientname']} you have appointment with {COMMON_ATTRIBUTES['doctorname']}"
