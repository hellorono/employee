# Generated by Django 4.1.1 on 2023-03-19 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0015_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
