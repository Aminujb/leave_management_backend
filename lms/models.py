from django.contrib.auth.models import User
from django.db import models


class Leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    date_applied = models.DateField(auto_now_add=True)
    leave_type = models.CharField(max_length=20)
    note = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='Leaves', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_applied']
