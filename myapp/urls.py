from django.urls import path 
from.views import home, python, test, temp1, portfolio

urlpatterns = [
    path("python/", python),
    path ("hello/", home),
    path ("test/", test),
    path ("", temp1),
    path ("portfolio/", portfolio)
]
