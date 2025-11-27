from django import forms
from .models import *

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ["device_name", "device_type", "serial_number", "status", "location", "ip_address", "installation_date", "last_maintenance", "notes"]