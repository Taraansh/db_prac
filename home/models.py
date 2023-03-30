from django.db import models

# Create your models here.
class employees(models.Model):
    emp_id = models.AutoField(primary_key=True, null=False)
    emp_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)

    def __str__(self):
        return self.emp_name
    