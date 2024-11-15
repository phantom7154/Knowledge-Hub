from django.db import models

# Create your models here.  

class Contact(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=100)  # Adjust as needed
    confirmpassword = models.CharField(max_length=100)


    def __str__(self):
        return self.username  # Use 'self.username' since 'name' doesn't exist

class Meta:
    db_table = "contact"