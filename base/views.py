from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserForm
from .models import Games,BattleRoyale
# Create your views here.
def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    context = {'form':form}
    return render(request,'base/register.html',context)

def home(request):
    #game = Games.objects.all()
    context = {}
    return render(request,'base/Home.html',context)
def gaming_profile(request,pk):
    game_pf = BattleRoyale.objects.filter(Game__name=pk)
    context = {'pf':game_pf}
    return render(request,'base/profile.html',context)

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('after_login')
    context={}
    return render(request,'base/Login.html',context)

def fun(request):
    return render(request,'base/main.html')