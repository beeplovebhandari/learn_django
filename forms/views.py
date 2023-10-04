from django.shortcuts import render, redirect
from tables.models import Students, Item 
from crud.models import ClassRoom
from .form import ClassRoomForm, ClassRoomModelForm

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


def classroom(request):
     if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
         name = form.cleaned_data.get("name")
         ClassRoom.objects.create(name=name)
         return redirect("forms_classroom")
        

     form = ClassRoomForm()
     classrooms = ClassRoom.objects.all()
     return render (request, template_name="forms/classroom.html" , context={"classrooms": classrooms,
                                                                             "form": form})

def model_classroom(request):
    if request.method == "POST":
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("forms_classroom")
    form = ClassRoomModelForm()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="forms/classroom.html", context={"form": form,
                                                                            "classrooms": classrooms})