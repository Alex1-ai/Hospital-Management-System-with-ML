import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User, Group

@pytest.mark.django_db
def test_heart_disease_prediction_view(client):
    # Create a user and login
    user = User.objects.create_user(username='testuser', password='password')
    client.force_login(user)

    # Prepare form data for a POST request
    form_data = {
        'age': '55',
        'sex': '0',
        'cp': '1',
        'trestbps': '132',
        'chol': '342',
        'fbs': '0',
        'restecg': '1',
        'thalach': '166',
        'exang': '0',
        'oldpeak': '1.2',
        'slope': '2',
        'ca': '0',
        'thal': '2'
    }

    # Make a POST request to the heart_disease_prediction view
    response = client.post(reverse('heartdisease'), form_data)

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the prediction is present in the response context
    # print(" result oooh ",response.context[0])
    assert "message" in response.context["context"]
    # assert  response.context.message == 'The result shows this patient is positive'

    # Check if the prediction message is correct (assuming the message format is known)
    # Example: assert response.context['message'] == 'The person does not have a Heart Disease'

    # You can also check other aspects of the response as needed
