import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from sitehandler.views import loginpage

@pytest.mark.django_db
def test_loginpage_view(client):
    # Create users and assign them to different groups
    doctor_user = User.objects.create_user(username='doctor@example.com', password='password')
    doctor_group = Group.objects.create(name='Doctor')
    doctor_user.groups.add(doctor_group)

    receptionist_user = User.objects.create_user(username='receptionist@example.com', password='password')
    receptionist_group = Group.objects.create(name='Receptionist')
    receptionist_user.groups.add(receptionist_group)

    patient_user = User.objects.create_user(username='patient@example.com', password='password')
    patient_group = Group.objects.create(name='Patient')
    patient_user.groups.add(patient_group)

    # Prepare form data for a POST request
    form_data_doctor = {
        'email': 'doctor@example.com',
        'password': 'password'
    }

    form_data_patient = {
        'email': 'patient@example.com',
        'password': 'password'
    }

    form_data_receptionist = {
        'email': 'receptionist@example.com',
        'password': 'password'
    }
    
    
    
    # Make a POST request to the loginpage view with doctor's credentials
    response_doctor = client.post(reverse('loginpage'), form_data_doctor)

    # Check if the response status code is 200
    assert response_doctor.status_code == 200

    # Check if the user is logged in and redirected to the correct page
    assert response_doctor.context['page'] == 'doctor'
    assert response_doctor.context["error"] == 'no'

    # Repeat the same process for receptionist and patient users
    # Make a POST request to the loginpage view with doctor's credentials
    response_patient = client.post(reverse('loginpage'), form_data_patient)

    # Check if the response status code is 200
    assert response_patient.status_code == 200

    # Check if the user is logged in and redirected to the correct page
    assert response_patient.context['page'] == 'patient'
    assert response_patient.context["error"] == "no"

    # check fi the user logged in is receptionist
    response_receptionist = client.post(reverse('loginpage'), form_data_receptionist)

    # Check if the response status code is 200
    assert response_receptionist.status_code == 200

    # Check if the user is logged in and redirected to the correct page
    assert response_receptionist.context['page'] == 'reception'
    assert response_receptionist.context["error"] == "no"

 
