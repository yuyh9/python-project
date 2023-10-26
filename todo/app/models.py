from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# title
# status
# data - current
# user
# priority

class Todo(models.Model):
    status_choices = [
        ('C', 'Complete'),
        ('P', 'Pending'),
    ]
    priority_choices = [
        (1, '1️⃣'),
        (2, '2️⃣'),
        (3, '3️⃣'),
        (4, '4️⃣'),
        (5, '5️⃣'),
        (6, '6️⃣'),
        (7, '7️⃣'),
        (8, '8️⃣'),
        (9, '9️⃣'),
        (10, '🔟'),
        
    ]
    title = models.CharField(max_length=50)
    todo_detail = models.TextField(blank=True)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=priority_choices, default=1)
