from django.urls import path
from.views import student_view, items_view

urlpatterns=[
    path('', student_view, name = "student_view"),
    path ('items/', items_view, name = "items_forms")
]