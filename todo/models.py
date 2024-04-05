from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=30)
    body = models.TextField()

    owner = models.ForeignKey(
        to = User ,
        on_delete = models.CASCADE 
    )

    status = models.BooleanField(default =False)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)



    def __str__(self):

        return f"{self.title}-{self.owner}"