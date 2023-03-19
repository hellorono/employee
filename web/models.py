from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    emp_no=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    emp_start_date=models.DateField()
    emp_end_date=models.DateField(null=True)
    photo=models.ImageField(upload_to='photo',null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name
