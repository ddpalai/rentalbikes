from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    age = models.IntegerField()
    driving_license_number = models.CharField(max_length=50)
    aadhar_card = models.IntegerField()
    address = models.TextField()
    vehicle_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
