from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        STUDENT = "student","Student"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
         default=Role.ADMIN,
        null=True
    )
    class Meta:
        db_table='users'

class Exam(models.Model):
    class Choose(models.TextChoices):
     MHQ = "MHQ", "MHQ" 
     TRUEORFALSE = "true/false","true/flase"
     essay='essay','Essay'
    title = models.CharField(max_length=200)
    type=models.CharField(max_length=20,choices=Choose.choices,default=Choose.MHQ)
    question_text = models.TextField()
    answer = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    timer = models.IntegerField()
    point = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='exam'

class Question(models.Model):
 

    class Meta:
        db_table='questions'


class ExamAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    numbeOfAttemp=models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)