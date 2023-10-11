from django.urls import path
from .views import FirstView, ClassRoomTemplateView, ClassRoomView, StudentView, StudentDetailView

urlpatterns=[
    path("classroom/", ClassRoomView.as_view(), name="classbased_classroom"),
    path("add_student/", StudentView.as_view(), name="classbased_add_student"),
    path("student/", StudentView.as_view(), name="classbased_student"),
    path("student-detail/<int:pk>/", StudentDetailView.as_view(), name="classbased_student_detail"),
    path('class-temp/', ClassRoomTemplateView.as_view(), name="class_temp"),
    path("", FirstView.as_view(), name="first_view")
]