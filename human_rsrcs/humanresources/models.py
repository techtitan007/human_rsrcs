from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Employee(models.Model):
    profile_picture = models.ImageField(upload_to='employees/', storage=MediaStorage())
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)

   
    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class MediaStorage(S3Boto3Storage):
    location = 'media'

    def _str_(self):
	return self.name
