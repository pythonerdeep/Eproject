
from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from .models import User
# Create your views here.
def sign(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('h/')
        messages.add_message(request,message.INFO,'Customer Added Successfully !')
    return render(request,'signup.html',{'form':form})

def login(req):
    form=LoginForm(req.POST or None)
    if form.is_valid():
        email1=form.cleaned_data.get('email')
        password1=form.cleaned_data.get('password')
        print(email1,password1)

        r=User.objects.filter(email=email1,password=password1)
        if r:
            req.session['em']=email1
            print('data match')
            return redirect ('/dash')
        else:
            print('data not match')
    context={
        'form':form
    }
    return render(req,'login.html',context)

def dashboard(request):
    return render(request,'dashboard.html')