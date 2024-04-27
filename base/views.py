from django.shortcuts import render
# from .forms import CustomUSerForm
# Create your views here.
def home(request):
    return render(request,'base/main.html')

def register(request):
    # form = CustomUSerForm()
    context = {}
    return render(request,'base/register.html',context)