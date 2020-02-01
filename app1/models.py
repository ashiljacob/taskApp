from datetime import date

from django.db import models

from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)
    added_date = models.DateField(default=date.today())
    comment = models.TextField(max_length=20)
    created = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title


