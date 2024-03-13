from django.urls import reverse, resolve
from sitehandler.views import homepage

def test_homepage_url():
    # Get the URL for the homepage view
    url = reverse('homepage')

    # Resolve the URL to a view function
    resolver = resolve(url)

    # Check if the resolved view function matches the expected view function
    assert resolver.func == homepage
