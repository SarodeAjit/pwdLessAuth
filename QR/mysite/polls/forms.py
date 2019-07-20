from django import forms 
from .models import *

class QrCodeForm(forms.ModelForm): 
  
    class Meta: 
        model = cQrCode 
        fields = ['uniqueId', 'QrCodeImg_name'] 