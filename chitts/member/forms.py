# forms.py
from django import forms
from .models import Person
from .models import InterestInput

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'age', 'parentname']
class InterestInputForm(forms.ModelForm):
    class Meta:
        model = InterestInput
        fields = ['principal_amount']