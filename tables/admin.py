from django.contrib import admin
from .models import Students,Item, StudentProfile

admin.site.register(Students)
admin.site.register(StudentProfile)

admin.site.register(Item)