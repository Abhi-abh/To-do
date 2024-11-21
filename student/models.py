from django.db import models

# Create your models here.

class insert_details(models.Model):
    student_name = models.CharField(max_length=250)
    student_email = models.EmailField()
    student_age = models.PositiveIntegerField(max_length=10)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return self.student_name