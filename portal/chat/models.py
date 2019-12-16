import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class counsellor(AbstractUser):

    user_status = models.BooleanField(default=False)
    user_information = models.TextField(max_length=1000)
    user_dp = models.ImageField(
        upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.username


class student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_status = models.BooleanField(default=False)


class Chatroom(models.Model):
    Chatroom_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    Counsellor = models.ForeignKey(counsellor, on_delete='SET_NULL')
    Student = models.ForeignKey(student, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    abort = models.BooleanField(default=False)


class messages(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField(max_length=1000)
    message_from = models.BooleanField(default=0)
    # chat_session = models.ForeignKey(Chatroom, on_delete=models.CASCADE) # add this later
    # message_time = models.DateTimeField()                                # add this later
