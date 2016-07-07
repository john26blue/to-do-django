from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('a', 'Submitted'),
    ('b', 'Started'),
    ('c', 'Finished'),
    )
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    added_date = models.DateField(auto_now_add=True)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return self.content