from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)
    last_update = models.DateTimeField(auto_now=True, editable=True)
    is_active = models.BooleanField(default=True)
    path = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

