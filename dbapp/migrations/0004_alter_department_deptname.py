# Generated by Django 5.1.6 on 2025-03-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0003_department_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deptname',
            field=models.CharField(max_length=20),
        ),
    ]
