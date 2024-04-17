from django.db import models

# The models are created here
class Task(models.Model):
    
    # Unique identifier of the task
    id = models.AutoField(primary_key=True)

    # The name of the task
    name = models.CharField(max_length=100, unique=True)

    # A dude date
    dueDate = models.DateField(blank=True, null=True) 
    
    # A boolean flag to indicate if the task is on completed or not
    status = models.BooleanField(default=False)