from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

def home(request):
    townships = Township.objects.all()
    towns = Town.objects.all()
    villages = Village.objects.all()
    wards = Ward.objects.all()
    context = {
        'townships':townships,
        'villages':villages,
        'towns':towns,
        'wards':wards
        
    }
    return render(request, 'layout/index.html', context)

# township

def create_township(request):
    township = Township.objects.all()
    form = TownshipForm()
    if request.method =='POST':
        form = TownshipForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('township_page')
    context = {
        'form':form,
        'township':township
        
        }
    return render(request, 'township/create.html', context)
    
    
    
    
def township(request):
    villages = Village.objects.all()
    towns = Town.objects.all()
    townships = Township.objects.all()
    wards = Ward.objects.all()
    context = {
        'townships':townships,
        'villages':villages,
        'towns':towns,
        'wards':wards
    }
    return render(request, 'township/township.html', context)

def township_detail(request, pk=id):
    township = Township.objects.filter()
    villages = Village.objects.filter(township_id=pk)
    context = {
        'township':township,
        'villages':villages,
        
    }
    return render(request, 'township/township_detail.html', context)

# towns 
def towns(request):
    townships = Township.objects.all()
    towns = Town.objects.all()
    wards = Ward.objects.all()
    context = {
        'towns':towns,
        'wards':wards,
        'townships':townships,
    }
    return render(request, 'township/towns.html', context)

def town_detail(request, pk=id):
    town = Town.objects.filter()
    wards = Ward.objects.filter(town_id=pk)
    context ={
        'town':town, 
        'wards':wards
    }
    return render(request, 'township/town_detail.html', context)

# village
def create_village(request):
    form = VillageForm
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('township_page')
    context = {
        'form':form,
    }
    return render(request, 'village/create_village.html', context)
