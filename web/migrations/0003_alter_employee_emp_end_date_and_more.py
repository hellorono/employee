# Generated by Django 4.1.1 on 2023-03-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_employee_emp_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_end_date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_start_date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
