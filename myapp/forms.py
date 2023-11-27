from django import forms
from .models import Plant
from .models import Greenhouse
from .models import PlantType
from .models import InGreenhouse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class InGreenhouseForm(forms.ModelForm):
    cell = forms.CharField(widget=forms.HiddenInput())
    plant = forms.ModelChoiceField(queryset=Plant.objects.all())
    
    class Meta:
        model = InGreenhouse
        fields = ['plant', 'cell']  
        exclude = ['user','planting_date']

class PlantForm(forms.ModelForm):
    plant_type = forms.ModelChoiceField(queryset=Plant.objects.all())
    
    class Meta:
        model = PlantType
        fields = ['plant_type']

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'shadow appearance-none border-2 border-blue-500 rounded w-full px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'shadow appearance-none border-2 border-blue-500 rounded w-full px-3 mb-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ['rows', 'row_length']