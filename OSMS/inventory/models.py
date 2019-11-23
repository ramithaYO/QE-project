from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#here post is a table 
class Items(models.Model):
    name=models.CharField(max_length=100)
    description =models.TextField()
    productdetails =models.TextField()
    numberofitems=models.IntegerField()
    availability=models.BinaryField()
    #date_posted=models.DateTimeField(default=timezone.now)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    # item=models.OneToOneField(Items,on_delete=models.CASCADE)
    item=models.OneToOneField(Items, on_delete=models.CASCADE)
    # image=models.ImageField(default='default.jpg',upload_to='item_pics')
    image=models.ImageField(default='default.jpg', upload_to='item_pics') 

    def __str__(self):
        return f'{self.item.name} profile'



