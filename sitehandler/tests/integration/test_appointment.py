import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User, Group
from sitehandler.models import Doctor, Appointment
from datetime import date

@pytest.mark.django_db
def test_make_appointments_view(client):
    # Create a patient user
    patient_user = User.objects.create_user(username='patient@example.com', password='password')    
    patient_group = Group.objects.create(name='Patient')
    patient_user.groups.add(patient_group)
    client.force_login(patient_user)

    # Create some doctors for testing
    doctor = Doctor.objects.create(
        name='Dr. Smith',
        email='smith@example.com',
        password='password',
        gender='Male',
        phonenumber='1234567890',
        address='123 Main St',
        birthdate=date(1980, 1, 1),
        bloodgroup='O+',
        specialization='Cardiologist'
    )

    # Test GET request
    response_get = client.get(reverse('makeappointments'))
    assert response_get.status_code == 200
    assert 'alldoctors' in response_get.context

    # Test POST request
    form_data = {
        'doctoremail': 'smith@example.com',
        'doctorname': 'Dr. Smith',
        'patientname': 'John Doe',
        'patientemail': 'john@example.com',
        'appointmentdate': '2024-03-15',
        'appointmenttime': '10:00',
        'symptoms': 'Chest pain'
    }
    response_post = client.post(reverse('makeappointments'), form_data)
    assert response_post.status_code == 200
    assert 'error' in response_post.context  # Assuming error message is returned in context
    assert Appointment.objects.count() == 1  # Check if an appointment is created
