import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

@pytest.fixture
def client():
    return Client()

def test_homepage_view(client):
    response = client.get(reverse('homepage'))
    assert response.status_code == 200
    assert 'index.html' in [template.name for template in response.templates]
    
@pytest.mark.django_db
def test_login_admin_view(client):
    # Create a sample staff user for testing login admin view
    User.objects.create_user(username='admin', password='adminpassword', is_staff=True)

    # Authenticate the client
    client.login(username='admin', password='adminpassword')

    response = client.get(reverse('login_admin'))
    assert response.status_code == 200
    assert 'adminlogin.html' in [template.name for template in response.templates]

# Add more tests for other views as needed
