import pytest
from django.test import RequestFactory
from django.shortcuts import render
from django.urls import reverse

@pytest.mark.django_db
def test_aboutpage_contains_about_us_text(client):
    # Make a GET request to the aboutpage view
    response = client.get(reverse('aboutpage'))
    
    # Ensure that the response status code is 200
    assert response.status_code == 200
    
    # Check if the response content (HTML) contains the word "About"
    assert b"About Us" in response.content
