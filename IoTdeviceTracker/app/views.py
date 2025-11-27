from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def device_list(request):
    devices = Device.objects.all()
    return render(request, "device/device_list.html", {"devices" : devices})

def device_create(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("device_list")
        else:
            return render(request, 'device/device_create.html', {'form': form})
    else:
        form = DeviceForm()
        return render(request, "device/device_create.html", {"form" : form})
    
def device_delete(request, pk):
    device = get_object_or_404(Device, pk = pk)
    if request.method == "POST":
        device.delete()
        return redirect("device_list")
    else:
        return render(request, "device/device_delete.html", {"device" : device})
    
def device_update(request, pk):
    device = get_object_or_404(Device, pk = pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance = device)
        if form.is_valid():
            form.save()
            return redirect("device_list")
    else:
        form = DeviceForm(instance = device)
        return render(request, "device/device_create.html", {"form" : form})