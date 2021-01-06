from django.db import models

# Create your models here.
class Teacherr(models.Model):
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    id1 = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        db_table = "TeacherDetails"
