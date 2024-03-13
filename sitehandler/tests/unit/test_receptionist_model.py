# tests/unit/test_models.py
import pytest
from sitehandler.models import Receptionist
from datetime import date

# Common attributes
RECEPTIONIST_ATTRIBUTES = {
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
def test_receptionist_creation():
    receptionist = Receptionist.objects.create(**RECEPTIONIST_ATTRIBUTES)
    for key, value in RECEPTIONIST_ATTRIBUTES.items():
        assert getattr(receptionist, key) == value

@pytest.mark.django_db
def test_receptionist_str_representation():
    receptionist = Receptionist.objects.create(**RECEPTIONIST_ATTRIBUTES)
    assert str(receptionist) == RECEPTIONIST_ATTRIBUTES['name']
