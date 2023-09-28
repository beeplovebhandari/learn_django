from django.shortcuts import render, redirect
from tables.models import Students, Item

def student_view(request):
    if request.method == "POST":
        name= request.POST.get('name')
        age= request.POST.get('age')
        email= request.POST.get('email')
        address= request.POST.get('address')
        bio= request.POST.get('bio')
        Students.objects.create(name=name, age=age, email=email, address=address, bio=bio)
        return redirect('student')

    return render(request, template_name='forms/student_view.html')

def items_view(request):
    if request.method =="POST":
        item_name=request.POST.get('item_name')
        company=request.POST.get('company')
        mfd=request.POST.get('mfd')
        best_before=request.POST.get('best_before')
        description=request.POST.get('description')
        Item.objects.create(item_name=item_name, company=company, mfd=mfd, best_before=best_before, description=description)
        return redirect('item')

    return render(request, template_name='forms/items_forms.html')
