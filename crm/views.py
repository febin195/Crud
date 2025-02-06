from django.shortcuts import render
from django.views.generic import View
from crm.models import StudentModel,User
from crm.forms import StudentForm,RegisterForm,Loginform
from django.contrib.auth import authenticate,login

# Create your views here.

class RegisterView(View):
    def get(self,request):
        form=RegisterForm
        return render(request,"register.html",{'form':form})
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request,"register.html")
        

class LoginView(View):
    def get(self,request):
        form=Loginform
        return render(request,"login.html",{'form':form})  

    def post(self,request):
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)   
            if user:
                login(request,user)
                return render(request,"create.html") 
            
            else:
                return render(request,"login.html",{'form':form})





class StudentCreate(View):
    def get(self,request):
        form=StudentForm
        return render(request,"create.html",{'form':form})
    
    def post(self,request):
        form=StudentForm(request.POST)
        if form.is_valid():
            StudentModel.objects.create(**form.cleaned_data)
            return render(request,"read.html")
        else:
            form=StudentForm
            return render(request,"create.html",{'form':form})   

class StudentRead(View):
    def get(self,request):
        data=StudentModel.objects.all()
        return render(request,"read.html",{'data':data}) 

class StudentUpdate(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=StudentModel.objects.get(id=id)
        form=StudentForm(instance=data)
        return render(request,"update.html",{'form':form})  

    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=StudentModel.objects.get(id=id)
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return render(request,"read.html")          
    
class StudentDelete(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        StudentModel.objects.get(id=id).delete()    
        return render(request,"read.html")
