from django.contrib import admin
from .models import Students,Item, StudentProfile, ClassRoom

admin.site.register(Students)
admin.site.register(StudentProfile)
admin.site.register(ClassRoom)

admin.site.register(Item)