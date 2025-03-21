# Generated by Django 5.1.6 on 2025-03-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0005_aadhar_driver_car_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=13)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='employeedup',
            fields=[
            ],
            options={
                'ordering': ['-empname'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dbapp.employee',),
        ),
    ]
