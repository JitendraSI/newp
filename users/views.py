from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import StudentRegistration
from . forms import UserRegisterForm
from .models import Users
from django.contrib.auth.decorators import login_required

# Create your views here.

def homeb(request):
    return render(request, 'users/home.html')

@login_required()
def profile(request):
    return render(request, 'users/profile.html')        

def register(request):
    if request.method == "POST":
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Hi {username},your account was created sucessfully')
             return redirect('homeb')
         
    else:
        form = UserRegisterForm()       
    return render(request, 'users/register.html',{'form':form})

   #TO DO LIST VIEWS
    # THIS FUNCTION WILL ADD
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['workname']
            pw = fm.cleaned_data['remark']
            reg= Users(name=nm , workname=em, remark=pw)
            reg.save()
    else:
        fm = StudentRegistration()
    stud =Users.objects.all()
          
    return render(request, 'users/addandshow.html',{'form':fm,'stu':stud})

# THIS FUNCTION WILL EDIT/UPDATE 
def update_data(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Users.objects.get(pk=id)   
        fm = StudentRegistration (instance=pi)
    return render(request, 'users/updatestudent.html',{'form':fm})


# THIS FUNCTION WILL DELETE
def delete_data(request,id):
    if request.method == 'POST':
        pi=Users.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') 