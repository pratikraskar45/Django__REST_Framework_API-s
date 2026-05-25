from django.db import models

# Create your models here.
class Society(models.Model):
    floor_no=models.CharField(max_length=5)
    room_no=models.CharField(max_length=10)
    room_owner=models.CharField(max_length=50)
    room_type=models.CharField(max_length=10)
    
    def __str__(self):
        return self.room_owner
    