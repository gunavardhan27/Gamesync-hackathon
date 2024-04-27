from django.shortcuts import render,redirect
from .forms import CustomUserForm
# Create your views here.
def home(request):

    return render(request,'base/main.html')

def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    context = {'form':form}
    return render(request,'base/register.html',context)