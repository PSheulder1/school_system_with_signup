from django.shortcuts import render, redirect

from .models import Student



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def welcome(request):
    return render(request, "welcome.html")



def add(request):

    if request.method=="POST":
        nom = request.POST.get('nom')
        addresse = request.POST.get('addresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        classe = request.POST.get('classe')

        data = Student(nom=nom, addresse=addresse, 
                       telephone=telephone, email=email,
                         image=image, classe=classe)
        data.save()

    return render(request, "add.html")


def login(request):
    return render(request, "login.html")


def signup(request):

    if request.method=="POST":
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        username= request.POST.get("username")
        email= request.POST.get("email")
        password= request.POST.get("password")

        verified = User.objects.filter(username=username).exists()
        if verified:
            return render(request, "signup.html", {"error": "user already exist. Please login..."})
        
        create = User.objects.create_user(first_name=first_name,
                                           last_name=last_name, username=username,
                                           email=email,
                                           password=password)
        redirect('welcome')
    
    return render(request, "signup.html")


def table(request):
    data = Student.objects.all()
    return render(request, "table.html", {'data':data} )





