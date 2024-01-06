from django.db import models

# Create your models here.
class menu(models.Model):
  title = models.CharField(max_length = 255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.PositiveIntegerField()
  
  def __str__(self):
    return self.title
  
  
class booking(models.Model):
  name = models.CharField(max_length = 255)
  no_of_guests = models.IntegerField()
  bookingdate = models.DateTimeField()
  
  def __str__(self):
    return f"{self.name}'s Booking"