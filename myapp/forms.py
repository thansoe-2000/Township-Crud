from .models import *
from django import forms
from django.forms import ModelForm

class TownshipForm(forms.ModelForm):
    class Meta:
        model = Township
        fields = '__all__'
        labels = {
            'name':'မြို့နယ် နာမည်'
        }
        widget = {
            'name':forms.TextInput(attrs=({'placeholder':'မြို့နယ်နာမေ ထည့်ပါ။'})),
        }
      
        
class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        labels = {
            'township':'မြို့နယ်',
            'schools':'ကျောင်း',
            'houses':'အိမ်',
            'populations':'လူဦးရေ',
            'monestaries':'ဘုန်းကြီးကျောင်း',
            'name':'ရွာနာမည်',
        }
            
        widgets = {
         
         'schools':forms.NumberInput(attrs=({'placeholder':'စာသင်ကျောင်းအရီအတွက် ရိုက်ထည့်ပါ'})),
         'houses':forms.NumberInput(attrs=({'placeholder':'အိမ် အရီအတွက် ရိုက်ထည့်ပါ'})),
         'populations':forms.NumberInput(attrs=({'placeholder':'လူဦးရေ အရီအတွက် ရိုက်ထည့်ပါ'})),
         'monestaries':forms.NumberInput(attrs=({'placeholder':'ဘုန်းကြီးကျောင်းအရီအတွက် ရိုက်ထည့်ပါ'})),
         'name':forms.TextInput(attrs=({'placeholder':'ရွာ နာမေ ရိုက်ထည့်ပါ'})),
         
      }
        
       
      
    