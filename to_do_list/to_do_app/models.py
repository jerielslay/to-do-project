from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Tag(models.Model):
    name  = models.CharField(max_length=30, unique=True)


class Task(models.Model):
    description = models.CharField(max_length=255)
    #used only for many to many table relationships, when choosing which model to put it on consider how data is being presented, in finished product in this case when you are lookijng at a task you want to see all the tags attached to the task so we are adding this here.
    tags = models.ManyToManyField(Tag)

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #the moment you add a comment set time 
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    #(what do you want the foreign key attatched To and, what do you want to do when task is deleted)