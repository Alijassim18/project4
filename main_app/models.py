from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin" # value saved in db, value shown to the user
        Student = "student","Student"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        # default=Role.CUSTOMER,
        null=True
    )
    class Meta:
        db_table='user'

class Exam(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    timer = models.IntegerField()
    grade = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='exam'

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer = models.TextField()

    class Meta:
        db_table='questions'


class ExamAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    numbeOfAttemp=models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)