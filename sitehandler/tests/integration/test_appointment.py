# import pytest
# from django.test import Client
# from django.contrib.auth.models import User, Group
# from sitehandler.models import Appointment
# from django.utils import timezone

# @pytest.fixture
# def client():
#     return Client()


# @pytest.mark.django_db
# def test_viewappointments_patient(client):
#     # Create a sample user and assign them to the 'Patient' group
#     user = User.objects.create_user(username='patient_user', password='password')
#     patient_group = Group.objects.create(name='Patient')
#     patient_group.user_set.add(user)

#     # Create a sample appointment for the patient user
#     appointment = Appointment.objects.create(
#         patientemail=user,
#         appointmentdate=timezone.now() + timezone.timedelta(days=1),
#         status=True
#     )

#     # Log in the user
#     client.login(username='patient_user', password='password')

#     # Make a GET request to the view
#     response = client.get('/viewappointments/')

#     # Check that the response status code is 200 (OK)
#     assert response.status_code == 200

#     # Check that the upcoming appointment is present in the rendered content
#     assert str(appointment.appointmentdate) in response.content.decode()

# @pytest.mark.django_db
# def test_viewappointments_doctor(client):
#     # Create a sample user and assign them to the 'Doctor' group
#     user = User.objects.create_user(username='doctor_user', password='password')
#     doctor_group = Group.objects.create(name='Doctor')
#     doctor_group.user_set.add(user)

#     # Create a sample appointment for the doctor user
#     appointment = Appointment.objects.create(
#         doctoremail=user,
#         appointmentdate=timezone.now() + timezone.timedelta(days=1),
#         status=True
#     )

#     # Log in the user
#     client.login(username='doctor_user', password='password')

#     # Make a GET request to the view
#     response = client.get('/viewappointments/')

#     # Check that the response status code is 200 (OK)
#     assert response.status_code == 200

#     # Check that the upcoming appointment is present in the rendered content
#     assert str(appointment.appointmentdate) in response.content.decode()

# @pytest.mark.django_db
# def test_viewappointments_receptionist(client):
#     # Create a sample user and assign them to the 'Receptionist' group
#     user = User.objects.create_user(username='receptionist_user', password='password')
#     receptionist_group = Group.objects.create(name='Receptionist')
#     receptionist_group.user_set.add(user)

#     # Create a sample appointment for testing
#     appointment = Appointment.objects.create(
#         appointmentdate=timezone.now() + timezone.timedelta(days=1),
#         status=True
#     )

#     # Log in the user
#     client.login(username='receptionist_user', password='password')

#     # Make a GET request to the view
#     response = client.get('/viewappointments/')

#     # Check that the response status code is 200 (OK)
#     assert response.status_code == 200

#     # Check that the upcoming appointment is present in the rendered content
#     assert str(appointment.appointmentdate) in response.content.decode()
