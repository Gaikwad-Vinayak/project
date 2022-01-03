from django import forms
from .models import mode
class datat(forms.ModelForm):
    class Meta:
        model=mode
        fields=['name','email','password']
        widgets={
            
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        
        }