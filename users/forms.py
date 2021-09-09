from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()




    class Meta:
       model = User
       fields = ['username','email','password1','password2']  



 #TO DO LIST FORMS
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','workname','remark']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'workname': forms.TextInput(attrs={'class':'form-control'}),
            'remark': forms.TextInput(attrs={'class':'form-control'}),   
        }

         