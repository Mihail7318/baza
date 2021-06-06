from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def accom(request):
    return render(request, "accommodation.html")

def contact(request):
    return render(request, "contact.html")

def book(request):
    return render(request, "guest-book.html")