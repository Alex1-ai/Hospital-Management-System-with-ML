from django.test import Client
import pytest


@pytest.fixture
def user_data():
    """
      Getting user data so it can be utilized in tests cases
    """
    return {
        "name":"user_name",
        "email":"user_email",
        "password":"user_password",
        "repeatpassword":"user-password",
        "gender":"usergender",
        "phonenumber":"0500040330",
        "address":"user_address",
        "dateofbirth":"2001-03-12",
        "bloodgroup":"A"



    }



@pytest.fixture
def client():
    return Client()


# @pytest.fixture
# def create_test_user()