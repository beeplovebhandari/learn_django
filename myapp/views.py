from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Hello World </h1>")

def python (request):
   return render (request , template_name = "tero.html")

def test (request):
    # we can send query strings/query parameters in the urls
    # Everything sent after "?" in the url is querystring 
    # Query string can be multiple and seperated by amperstand(&) 
    name =request.GET.get("name")
    return HttpResponse(f"<h1> Hello my name is {name}</h1>")

def temp1 (request):
    table_heading = "People Information"
    peoples_info =[
    {"first" : "john", "last" : "chor", "address" : "ktm"}, 
    {"first" : "tero", "last" : "fata", "address" : "pkr"},
    {"first" : "ram", "last" : "daka", "address" : "plp"},
    {"first" : "shyam", "last" : "gadha", "address" : "btl"}
    ]
    return render (request , template_name = "temp1.html", context = {"heading": "People Information",  "infos": peoples_info})

def portfolio(request):
    return render (request, template_name="myapp/index.html")