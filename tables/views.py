from django.shortcuts import render
from.models import Students, Item, StudentProfile

def student(request):
    students = Students.objects.all()
    return render (request , template_name = "tables/student.html", context={"students": students})

def profile (request):
    return render (request, template_name="tables/profile.html", context= {"profiles":StudentProfile.objects.all} )

def item(request):
    a = Item.objects.all()
    return render (request, template_name="tables/items.html", context={"items":a})