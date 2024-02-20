from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Receptionist(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Diabetes_Prediction(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	pregnancies = models.IntegerField(validators=[MinValueValidator(0)])
	glucose = models.IntegerField(validators=[MinValueValidator(0)])
	blood_pressure = models.IntegerField(validators=[MinValueValidator(0)])
	skin_thickness = models.IntegerField(validators=[MinValueValidator(0)])
	insulin = models.IntegerField(validators=[MinValueValidator(0)])
	bmi  = models.DecimalField(max_digits=5, decimal_places=2)
	diabetes_pedigree_func = models.DecimalField( max_digits=5, decimal_places=2)
	age = models.IntegerField(validators=[MinValueValidator(0)])
	outcome = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
	

class Heart_Disease_Prediction(models.Model):
	patient = models.ForeignKey(Patient,on_delete= models.CASCADE)
	age = models.IntegerField( validators=[MinValueValidator(1)])
	gender = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
	cp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
	trestbps = models.IntegerField()
	chol = models.IntegerField()
	fbs = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
	restecg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
	thalach = models.IntegerField()
	exang = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
	oldpeak = models.DecimalField(max_digits=5, decimal_places=2)
	slope = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
	ca = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
	thal = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
	target = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    

	def hasHeartDisease(self):
		if self.target == 0:
			return False
		else:
			return True


	def __str__(self) :
		return f"{self.patient.name} {self.hasHeartDisease(self.target) }"


class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	doctoremail = models.EmailField(max_length=50)
	patientname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	status = models.BooleanField()
	prescription = models.CharField(max_length=200)
	
	def __str__(self):
		return self.patientname+" you have appointment with "+self.doctorname