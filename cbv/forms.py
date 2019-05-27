from django import forms
from .models import CategoryModel

class Categoryform(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields="__all__"
        choices=(('Active','Active'),('Inactive','Inactive'))
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':4}),
            'status':forms.Select(choices=choices,attrs={'class':'form-control'})
        }