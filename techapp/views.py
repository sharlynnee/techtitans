from django.shortcuts import render,redirect
from techapp.models import Users

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user = Users(fullname=request.POST['fullname'],
                     username=request.POST['username'],
                     password=request.POST['password'],
                     email=request.POST['email']
                     )
        user.save()
        return redirect('/login')
    else:
        return render(request,'register.html')

