from django import forms
from appsix.models import form_org

class form_new(forms.ModelForm):
    class Meta():
        model = form_org
        fields = '__all__'