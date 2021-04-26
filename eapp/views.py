from django.shortcuts import render,redirect
from .models import Name
from django.contrib import messages
from .forms import NameForm,IdForm,CompanyForm,InformationForm,VenueForm,DomainForm,LoginForm
from django.core.mail import send_mail
from django.conf import settings
import random
import requests
import json
# Create your views here.

def form(request):
    if request.method=='POST':
        form=NameForm(request.POST or None)
        if form.is_valid():
            form.save()

            em =form.cleaned_data.get('email')
            pas=form.cleaned_data.get('password')
            subject='Registration.'
            message='Welcome to the our website.\n Thanks foe choosing our services.''\n'+'Your Login ID :'+em +'\n' 'Your password:'+pas
            from_email=settings.EMAIL_HOST_USER
            recipient_list=[em]
            send_mail(subject,message,from_email,recipient_list)
            return redirect('/f2')
    else:
        form=NameForm()
        return render(request,'forms.html',{'form':form})

def form2(request):
    if request.method=="POST":
        form=IdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/f3')
    else:
        form=IdForm()
    return render(request,'forms2.html',{'form':form})
def form3(request):
    if request.method=="POST":
        form=CompanyForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request,'Your information will be sent to our accountant for your better reference.')
            return redirect('/f4')
    else:
        form=CompanyForm()
    return render(request,'form3.html',{'form':form})
def form4(request):
    if request.method=="POST":
        form=InformationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/f5')
    else:
        form=InformationForm()
    return render(request,'forms4.html',{'form':form})

def location(request):
    if request.method=="POST":
        form=VenueForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/f5')
    else:
        form=VenueForm()
    return render(request,'location.html',{'form':form})

def form5(request):
    if request.method=="POST":
        form=DomainForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/sub')
    else:
        form=DomainForm()
    return render(request,'form5.html',{'form':form})

def submit(request):
    return render(request,'submit.html')

def login(req):
    form=LoginForm(req.POST or None)
    if form.is_valid():
        email1=form.cleaned_data.get('email')
        password1=form.cleaned_data.get('password')

        r=Name.objects.filter(email=email1,password=password1)
        if r:
            req.session['em']=email1
            print('data match')
            return redirect ('/otp')
        else:
            print('data not match')
    context={
        'form':form
    }
    return render(req,'login.html',context)

URL = 'https://sms.shinenetcore.com/vendorsms/pushsms.aspx'
m=random.randint(100000, 999999)
def otp(request):
    if 'mobile' in request.POST:
        mob=request.POST["mobile"]
        mes='Your OTP is : '+m.__str__()
        deep ={
            'clientid':'a850fc56-476e-4103-8f29-c870317ad4bd',
            'apikey': '6fc4611a-5a49-409d-b256-95d2e95123fd',
            'sid': 'SMSSNC',
            'fl': '0',
            'gwid': '2',
            'msisdn': mob,
            'msg': mes,
        }
        respone= requests.post(URL,deep)
        return redirect('/v',respone)
    return render(request,'otp.html')


def verify(request):
    if 'number' in request.POST:
        nu=request.POST["number"]
        url = 'https://sms.shinenetcore.com/vendorsms/verify.aspx?clientid=a850fc56-476e-4103-8f29-c870317ad4bd&apikey=6fc4611a-5a49-409d-b256-95d2e95123fd&fl=0&gwid=2' + 'm' + "/"+nu + ""
        response=requests.request("GET",url)
        data=response.json()
        if data['Status'] == "Success":
            login.is_active = True
            print("data matched")
        return redirect('/dash')
    else:
        print('data not matched')
        logout(request)
    return render(request,'varify.html')

def logout(request):
    if not request.session.get('email',None):
        return redirect('/login')
    del request.session['email']
    return redirect('/login')
