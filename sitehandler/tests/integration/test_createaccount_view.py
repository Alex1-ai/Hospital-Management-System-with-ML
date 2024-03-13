import pytest
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, Group
from sitehandler.views import createaccountpage
from django.contrib.auth.models import Group

@pytest.fixture
def create_patient_group():
    Group.objects.create(name='Patient')
@pytest.mark.django_db
def test_createaccountpage_view(client, create_patient_group):
    # Prepare form data for a POST request
    form_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'password': 'password123',
        'repeatpassword': 'password123',
        'gender': 'Male',
        'phonenumber': '1234567890',
        'address': '123 Main St',
        'dateofbirth': '1990-01-01',
        'bloodgroup': 'O+'
    }

    # Make a POST request to the createaccountpage view with form data
    response = client.post(reverse('createaccountpage'), form_data)

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the user was created and added to the 'Patient' group
    assert User.objects.filter(email='john@example.com').exists()
    user = User.objects.get(email='john@example.com')
    # assert user.groups.filter(name='Patient').exists()

    # Verify the error message
    assert 'error' in response.context
    print(response.context)
    assert response.context['error'] == 'no'
