from django.shortcuts import render,redirect
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
    game = Games.objects.all()
    context = {'game':game}


    return render(request,'base/main.html',context)
def gaming_profile(request,pk):
    game_pf = BattleRoyale.objects.filter(Game__name=pk)
    context = {'pf':game_pf}
    return render(request,'base/profile.html',context)