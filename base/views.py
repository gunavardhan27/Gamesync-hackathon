from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserForm
from .models import Games,BattleRoyale
from .filters import GameFilter
# Create your views here.
def home(request):
    return render(request,'base/home.html')
def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    
    context = {'form':form}
    return render(request,'base/register.html',context)
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

def game(request):
    game = Games.objects.all()
    context = {'game':game}
    return render(request,'base/main.html',context)

def filters(request):
    options = BattleRoyale.objects.all()
    data = GameFilter(request.GET,queryset=options)
    options=data.qs 
    context={'data':data,'set':options}
    return render(request,'base/filter.html',context)
