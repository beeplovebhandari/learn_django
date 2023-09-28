from django.shortcuts import render, redirect
from .models import ClassRoom


def crud_classroom(request):
    if request.method == "POST":
        name= request.POST.get('name')
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name= 'crud/classroom.html', 
                  context ={"classrooms": classrooms, "title": "Classroom"})


def classroom_delete(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        classroom.delete()
        return redirect('crud_classroom')
    return render(request, template_name="crud/classroom_delete.html", context={"classroom": classroom})

def classroom_update(request, id):
    classroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        name= request.POST.get("name")
        ClassRoom.objects.filter(id=id).update(name=name)
        return redirect("crud_classroom")

    return render(request, template_name="crud/classroom_update.html", context={"classroom": classroom})
