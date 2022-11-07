from django import forms
from .models import Patient


class EditForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide patient\'s status -- '),
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
        ('Treated', 'Treated'),
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    residence = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    national_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}))
    symptoms = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), disabled=True)
    disease =forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), disabled=True)
    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS, disabled=True)

    class Meta:
        model = Patient
        fields = '__all__'

class EditPatientInfoForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide patient\'s status -- '),
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
        ('Treated', 'Treated'),
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), disabled=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}), disabled=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}), disabled=True)
    residence = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), disabled=True)
    national_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}), disabled=True)
    symptoms = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    disease =forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS)

    class Meta:
        model = Patient
        fields = '__all__'