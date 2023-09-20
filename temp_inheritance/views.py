from django.shortcuts import render


def main(request):
    people = [
        {"name": "Ram", "age": 30,"address": "KTM"},
        {"name": "Hari", "age": 24,"address": "KTM"},
        {"name": "Sita", "age": 45,"address": "BKT"}
    ]
    
    return render (request, template_name= 'temp_inheritance/home.html', context = {"people": people})

def features(request):
    items = [
        {"name": "Laptop", "feature": "A portable computer that can be used anywhere. "},
        {"name": "Mouse", "feature": "A Clicking input device of computer. "},
        {"name": "Keyboard", "feature": "An input device with keys. "}
    ]
    return render (request, template_name= 'temp_inheritance/features.html', context = {"items" : items})

def pricing(request):
    items = [
        {"name": " Apple Macbook Air 14", "storage": "8/512gb", "price": "2,49,999"},
        {"name": "Acer Chromebook Spin 714", "storage": "8/256gb", "price":"1,85,999"},
        {"name": " Dell XPS 13 Plus", "storage": "12/512gb", "price": "2,99,999"},
        {"name": "Lenovo Yoga Slim 7Pro", "storage" : "4/128gb", "price": "99,999"}
    ]
    return render (request, template_name= 'temp_inheritance/pricing.html', context = {"items" : items})
