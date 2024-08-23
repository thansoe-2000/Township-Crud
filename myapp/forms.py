from .models import *
from django import forms
from django.forms import ModelForm

class TownshipForm(ModelForm):
    class Meta:
        model = Township
        fields = '__all__'
        labels = {
            'name':'Name'
        }
        widget = {
            'name':forms.TextInput(attrs=({'placeholder':'နာမေ ကို ရိုက်ထည့်ပါ'})),
        }
        
class VillageForm(ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        labels = {
            'schools':'Schools',
        }
        widget = {
            'schools':forms.TextInput(attrs={'placeholder':'ကျောင်းအရီအတွက် ရိုက်ထည့်ပါ။'})
        }
        def __init__(self, *args, **kwargs):
            super(VillageForm, self).__init__(*args, **kwargs)
       
      
    