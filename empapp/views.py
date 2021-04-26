from django.shortcuts import render,redirect
from .forms import EmployeeForm

# Create your views here.
def emp(request):
    pass
    if request.method=="POST":
        form=EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/sub')
    else:
        form=EmployeeForm()
    return render(request,'emp.html',{'form':form})