from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Priority(models.Model) :
    name = models.CharField(max_length=6,null=True)

    def __str__(self) :
        return self.name

class Difficulty(models.Model) :
    name = models.CharField(max_length=6,null=True)

    def __str__(self) :
        return self.name

class Status(models.Model) :
    name = models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.name




class Ideas(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )

    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL,null=True)
    description = models.CharField(max_length=2000,null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL,null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    linkedin_url = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.nickname
