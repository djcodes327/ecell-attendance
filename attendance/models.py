from django.db import models


# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=12)
    semester = models.IntegerField(blank=True, null=True)
    gr_no = models.IntegerField(blank=True)
    enrollment_no = models.IntegerField(blank=True)
    branch = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    last_login = models.DateTimeField()

    class Meta:
        db_table = "Student"
        ordering = ['-fname']
        verbose_name_plural = "Students"

    def __str__(self):
        return self.fname + "" + self.lname


class Machines(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
