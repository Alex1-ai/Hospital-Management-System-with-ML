# Generated by Django 3.0.4 on 2024-02-21 09:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0010_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heart_Disease_Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('gender', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('cp', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('restecg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('oldpeak', models.DecimalField(decimal_places=2, max_digits=5)),
                ('slope', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('ca', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('thal', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('target', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitehandler.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diabetes_Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('glucose', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('blood_pressure', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('skin_thickness', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('insulin', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diabetes_pedigree_func', models.DecimalField(decimal_places=2, max_digits=5)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('outcome', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitehandler.Patient')),
            ],
        ),
    ]
