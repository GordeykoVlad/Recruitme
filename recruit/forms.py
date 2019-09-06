from django import forms
from .models import Recruit
from django.core.exceptions import ValidationError


class NewRecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'planet', 'age', 'mail', 'planet']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'planet': forms.ModelChoiceField(queryset=Planet.objects.filter(),to_field_name="name"),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']
        if Recruit.objects.filter(name__iexact=new_name).count():
            raise ValidationError('Name must be unique. We have "{}" name already'.format(new_name))
        return new_name
