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
    page = 'create_township'
    township = Township.objects.all()
    form = TownshipForm()
    if request.method =='POST':
        form = TownshipForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('township_page')
    context = {
        'form':form,
        'township':township,
        'page':page,
        }
    return render(request, 'township/township_crud.html', context)

# update township
def update_township(request,pk):
    page = 'update_township'
    township = Township.objects.get(id=pk)
    form = TownshipForm(instance=township)
    
    if request.method == 'POST':
        form = TownshipForm(request.POST, instance=township)
        if form.is_valid():
            form.save()
        return redirect('township_page')
        
    context = {
        'form':form,
        'township':township,
        'page':page
    }
   
    return render(request, 'township/township_crud.html',context)
    
# delete village
def delete_township(request, pk):
    township = Township.objects.get(id=pk)
    page = 'delete_township'
    if request.method == 'POST':
            township.delete()
            return redirect('township_page')
    context = {
        'township':township,
        'page':page
    }
    return render(request, 'township/township_crud.html', context)
        
        
    
# townships
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

# townships detail
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
    return render(request, 'towns/towns.html', context)

# towns create
def create_town(request):
    page = 'create_town'
    form = TownForm()
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('towns_page')
    context = {
        'page':page,
        'form':form,
    }
    return render(request, 'towns/towns_crud.html', context)

# towns update
def update_town(request, pk):
    town = Town.objects.get(id=pk)
    page = 'update_town'
    form = TownForm(instance=town)
    if request.method == 'POST':
        form = TownForm(request.POST, instance=town)
        if form.is_valid():
            form.save()
        return redirect('towns_page')
    context = {
        'town':town,
        'page':page,
        'form':form,
    }
    return render(request, 'towns/towns_crud.html', context)

# town delete
def delete_town(request, pk):
    towns = Town.objects.all()
    town = Town.objects.get(id=pk)
    page = 'delete_town'
    if request.method == 'POST':
            town.delete()
            return redirect('towns_page')
    context = {
        'town':town,
        'page':page,
        'towns':towns
    }
    return render(request, 'towns/towns_crud.html', context)
        
        
# town detail
def town_detail(request, pk=id):
    town = Town.objects.filter()
    wards = Ward.objects.filter(town_id=pk)
    context ={
        'town':town, 
        'wards':wards
    }
    return render(request, 'towns/town_detail.html', context)

# village
def create_village(request):
    page = 'create_page'
    form = VillageForm()
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('township_page')
    context = {
        'form':form,
        'page':page
    }
    return render(request, 'village/village.html', context)

# update village
def update_village(request,pk):
    page = 'update_page'
    village = Village.objects.get(id=pk)
    form = VillageForm(instance=village)
    
    if request.method == 'POST':
        form = VillageForm(request.POST, instance=village)
        if form.is_valid():
            form.save()
        return redirect('township_page')
        
    context = {
        'form':form,
        'village':village,
        'page':page
    }
   
    return render(request, 'village/village.html',context)

# delete village
def delete_village(request, pk):
    village = Village.objects.get(id=pk)
    page = 'delete_village'
    if request.method == 'POST':
        village.delete()
        return redirect('township_page')
    context = {
        'village':village,
        'page':page,
    }
    return render(request, 'village/village.html', context)


# ward group
# ward create
def create_ward(request):
    wards = Ward.objects.all()
    page = 'create_ward'
    form = WardForm()
    if request.method == 'POST':
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('towns_page')
    context = {
        'wards':wards,
        'page':page,
        'form':form,
    }
    return render(request, 'ward/ward_crud.html', context)

# update_ward
def update_ward(request, pk):
    ward = Ward.objects.get(id=pk)
    page = 'update_ward'
    form = WardForm(instance=ward)
    if request.method == 'POST':
        form = WardForm(request.POST, instance=ward)
        if form.is_valid():
            form.save()
        return redirect('towns_page')
    context = {
        'ward':ward,
        'page':page,
        'form':form
    }
    return render(request, 'ward/ward_crud.html', context)

# delete_ward
def delete_ward(request, pk):
    ward = Ward.objects.get(id=pk)
    page = 'delete_ward'
    if request.method == 'POST':
        ward.delete()
        return redirect('towns_page')
    context = {
        'ward':ward,
        'page':page,
    }
    return render(request, 'ward/ward_crud.html', context)

# schools
def school(request):
    schooltypes = SchoolType.objects.all()
    context = {
        'schooltypes':schooltypes,
    }
    return render(request, 'school_type/school.html', context)

# create school
def create_school(request):
    schooltypes = SchoolType.objects.all()
    page = 'create_school'
    form = SchoolTypeForm()
    if request.method == 'POST':
        form = SchoolTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_page')
    context = {
        'schooltypes':schooltypes,
        'page':page,
        'form':form
    }
    return render(request, 'school_type/school_crud.html', context)

# update school type
def update_school_type(request, pk):
    schooltype = SchoolType.objects.get(id=pk)
    page = 'update_school'
    form = SchoolTypeForm(instance=schooltype)
    if request.method == 'POST':
        form = SchoolTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_page')
    context = {
        'schooltype':schooltype,
        'page':page,
        'form':form
    }
    return render(request, 'school_type/school_crud.html', context)


# delete school type
def delete_school_type(request, pk):
    page = 'delete_school_type'
    schooltype = SchoolType.objects.get(id=pk)
    if request.method == 'POST':
        schooltype.delete()
        return redirect('school_page')
    context = {
        'page':page,
        'schooltype':schooltype,
    }
    return render(request, 'school_type/school_crud.html', context)