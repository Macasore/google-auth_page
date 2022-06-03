from django.shortcuts import render

def home(request):
    return render(request, "lpage.html")

# Create your views here.
