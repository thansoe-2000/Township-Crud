from .models import *
from django import forms
from django.forms import ModelForm

class TownshipForm(ModelForm):
    class Meta:
        model = Township
        fields = '__all__'
        labels = {
            'name':'မြို့နယ် နာမည်'
        }
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'မြို့နယ်နာမေ ထည့်ပါ။'})),
        }
      
        
class VillageForm(ModelForm):
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
class TownForm(ModelForm):
    class Meta:
        model = Town
        fields = "__all__"
        labels = {
            'name':'မြို့နာမည်',
            'township':'မြို့နယ် နာမည်'
        }
        
class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields = "__all__"
        labels = {
            'name':'ရပ်ကွက်နာမည်',
            'town':'မြို့နာမည်',
            'schools':'စာသင်ကျောင်းအရီအတွက်',
            'houses':'အိမ်အရီအတွက်',
            'monestaries':'ဘုန်းကြီးကျောင်းအရီအတွက်',
        }
        
       
      
class SchoolTypeForm(ModelForm):
    class Meta:
        model = SchoolType
        fields = "__all__"
        labels = {
            'name':'ကျောင်း အမျိုးအစား'
        }
        widgets = {
            'name':forms.TextInput(attrs=({'placeholder':'‌ကျောင်းအမျိုးအစား ထည့်ပါ'})),
        }