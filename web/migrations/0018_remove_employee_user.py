# Generated by Django 4.1.1 on 2023-03-19 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_employee_emp_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]
