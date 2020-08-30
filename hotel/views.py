from django.shortcuts import render,redirect
from .models import RNac, Rac, Dac
# Create your views here.
def home(request):
    vac_rac= len(Rac.objects.filter(occopied=False))
    vac_rnac= len(RNac.objects.filter(occopied=False))
    vac_dac= len(Dac.objects.filter(occopied=False))
    context= {'vac_rac': vac_rac, 'vac_rnac': vac_rnac,'vac_dac':vac_dac}
    return render(request,'hotel/home.html',context)

def list(request):
    li_rac= Rac.objects.order_by('roomno')
    li_rnac= RNac.objects.order_by('roomno')
    li_dac= Dac.objects.order_by('roomno')
    context={'li_rac': li_rac, 'li_rnac': li_rnac,'li_dac':li_dac}
    return render(request,'hotel/list.html',context)

def vacatedrnac(request,id):
    if(request.method=="POST"):
        room=RNac.objects.get(id=id)
        room.occopied=False
        room.save()
        return redirect('list')

def bookedrnac(request,id):
    if(request.method=="POST"):
        room=RNac.objects.get(id=id)
        room.occopied=True
        room.save()
        return redirect('list')

def vacatedrac(request,id):
    if(request.method=="POST"):
        room=Rac.objects.get(id=id)
        room.occopied=False
        room.save()
        return redirect('list')

def vacateddac(request,id):
    if(request.method=="POST"):
        room=Dac.objects.get(id=id)
        room.occopied=False
        room.save()
        return redirect('list')

def bookedrac(request,id):
    if(request.method=="POST"):
        room=Rac.objects.get(id=id)
        room.occopied=True
        room.save()
        return redirect('list')

def bookeddac(request,id):
    if(request.method=="POST"):
        room=Dac.objects.get(id=id)
        room.occopied=True
        room.save()
        return redirect('list')
