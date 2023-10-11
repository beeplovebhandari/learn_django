from django.urls import path
from.views import hello_world, HelloWorldView, studentView, StudentFromDBView, StudentFromDBListView, ProfileFromDBListView,\
      ClassroomFromDBView, ClassRoomFromDBListView, StudentDetailView,\
          StudentListView, StudentProfileListView, ClassRoomAPIView, ClassRoomCreateAPIView, ClassRoomUpdateAPIView,\
              ClassRoomDetailAPIView, ClassRoomDeleteAPIView

urlpatterns=[
    path("hello-world/", hello_world),
    path("message/", HelloWorldView.as_view()),
    path("student/", studentView.as_view()),
     path("studnet-from-db/", StudentFromDBListView.as_view()),
    path("profile-from-db/", ProfileFromDBListView.as_view()),
    path("classroom-from-db/", ClassRoomFromDBListView.as_view()),
    path("student-list/", StudentListView.as_view()),
    path("student-profile-list/", StudentProfileListView.as_view()),
    path("studnet-from-db/<int:id>/", StudentFromDBView.as_view()),
    path("classroom-from-db/<int:id>/", ClassroomFromDBView.as_view()),
    path("student-detail/<int:id>/", StudentDetailView.as_view())   
]

generic_urls=[
    path("generic-classroom-list/", ClassRoomAPIView.as_view()),
    path("generic-classroom-create/", ClassRoomCreateAPIView.as_view()),
    path("generic-classroom-update/<int:pk>/", ClassRoomUpdateAPIView.as_view()),
    path("generic-classroom-detail/<int:pk>/", ClassRoomDetailAPIView.as_view()),
    path("generic-classroom-delete/<int:pk>/", ClassRoomDeleteAPIView.as_view()),


]

urlpatterns += generic_urls
