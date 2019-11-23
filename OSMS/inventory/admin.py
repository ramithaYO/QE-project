from django.contrib import admin

# Register your models here.
from .models import Items
from .models import Profile

admin.site.register(Items) 
admin.site.register(Profile) 
