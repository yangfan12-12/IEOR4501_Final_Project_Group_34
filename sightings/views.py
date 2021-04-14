from django.shortcuts import render
from .models import Sighting
from django.shortcuts import redirect
from .forms import SightingForm

def base_view(request):
    return render(request,'sightings/base.html', {})

def map(request):
    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings':sightings,
            }
    return render(request,'sightings/map.html',context)

def list(request):
    sightings = Sighting.objects.all()
    fields = ['Unique_Squirrel_Id','Date']
    context = {
        'sightings':sightings,
        'fields':fields
            }
    return render(request,'sightings/list.html',context)

def update(request,Unique_Squirrel_Id):
    sighting = Sighting.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance = sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SightingForm(instance = sighting)
    context = {
            'form':form,
            }
    return render(request, 'sightings/update.html', context)


def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SightingForm()

    context = {
            'form':form,
            }

    return render(request, 'sightings/add.html', context)

def stats(request):
    sightings = Sighting.objects.all()
  

    A = sightings.filter(Shift='AM').count()
    P = sightings.filter(Shift='PM').count()
    A_percentage = A/(A+P)
    P_percentage = P/(A+P)
    A = format(A,',')
    P = format(P,',')
    A_percentage = "{:.2%}".format(A_percentage)
    P_percentage = "{:.2%}".format(P_percentage)

    J = sightings.filter(Age='Juvenile').count()
    Ad = sightings.filter(Age='Adult').count()
    J_percentage = J/(J+Ad)
    Ad_percentage = Ad/(J+Ad)
    J = format(J,',')
    Ad = format(Ad,',')
    J_percentage = "{:.2%}".format(J_percentage)
    Ad_percentage = "{:.2%}".format(Ad_percentage)

    B = sightings.filter(Primary_Fur_Color='Black').count()
    G = sightings.filter(Primary_Fur_Color='Gray').count()
    C = sightings.filter(Primary_Fur_Color='Cinnamon').count()
    B_percentage = B/(B+G+C)
    G_percentage = G/(B+G+C)
    C_percentage = C/(B+G+C)
    B = format(B,',')
    C = format(C,',')
    G = format(G,',')
    B_percentage = "{:.2%}".format(B_percentage)
    G_percentage = "{:.2%}".format(G_percentage)
    C_percentage = "{:.2%}".format(C_percentage)

    Above = sightings.filter(Location='Above Ground').count()
    Ground = sightings.filter(Location='Ground Plane').count()
    Above_percentage = Above/(Above+Ground)
    Ground_percentage = Ground/(Above+Ground)
    Above = format(Above,',')
    Ground = format(Ground,',')
    Above_percentage = "{:.2%}".format(Above_percentage)
    Ground_percentage = "{:.2%}".format(Ground_percentage)

    T = sightings.filter(Running=True).count()
    F = sightings.filter(Running=False).count()
    T_percentage = T/(T+F)
    F_percentage = F/(T+F)
    T = format(T,',')
    F = format(F,',')
    T_percentage = "{:.2%}".format(T_percentage)
    F_percentage = "{:.2%}".format(F_percentage)
    
    context = {
            'Total':format(sightings.count(),','),
            'Shift':{'AM': A, 'PM': P},
            'Shift_Percentage':{'AM': A_percentage, 'PM': P_percentage},
            'Age': {'Juvenile': J, 'Adult': Ad},
            'Age_Percentage': {'Juvenile': J_percentage, 'Adult': Ad_percentage},
            'Primary_Fur_Color': {'Black':B, 'Gray':G, 'Cinnamon':C},
            'Primary_Fur_Color_Percentage': {'Black':B_percentage, 'Gray':G_percentage, 'Cinnamon':C_percentage},
            'Location': {'Above_Ground':Above, 'Ground_Plane':Ground},
            'Location_Percentage': {'Above_Ground':Above_percentage, 'Ground_Plane':Ground_percentage},
            'Running': {'True':T, 'False':F},
            'Running_Percentage': {'True':T_percentage, 'False':F_percentage},
    }
    return render(request, 'sightings/stats.html',{'context':context})

