# Generated by Django 4.2.4 on 2023-09-01 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('therapists', '0003_appointmenttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('full_name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('current_age', models.PositiveSmallIntegerField()),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])),
                ('appointment_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='therapists.appointmenttime')),
                ('site_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.siteuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]