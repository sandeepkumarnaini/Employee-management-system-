# Generated by Django 5.1.6 on 2025-03-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0007_employee_profile_pic_employee_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(null=True),
        ),
    ]
