from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()
    
    def submit(self):
       self.save()