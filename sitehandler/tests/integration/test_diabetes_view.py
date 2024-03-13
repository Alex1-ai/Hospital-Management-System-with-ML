import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
@pytest.mark.django_db
def test_diabetes_disease_prediction_view(client):
    # Create a user and login
    user = User.objects.create_user(username='testuser', password='password')
    client.force_login(user)
    
    # Prepare test data for the POST request
    post_data = {
        'pregnancy': '4',
        'glucose': '110',
        'bloodPressure': '92',
        'skinThickness': '0',
        'insulin': '0',
        'bmi': '37.6',
        'diabetesPedigreeFunc': '0.191',
        'age': '30'
    }

    # Send a POST request to the view
    response = client.post(reverse('diabetesdisease'), post_data)

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the 'message' key exists in the response context
    assert 'context' in response.context
    assert 'message' in response.context['context']

    # Check if the prediction message matches the expected value
    # expected_message = 'The result shows this patient is positive'
    # assert response.context['context']['message'] == expected_message
