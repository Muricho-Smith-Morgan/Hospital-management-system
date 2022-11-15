from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
      model = User
      fields = ('username', 'password1', 'password2')



class EditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    room_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_in = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_out = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))


    class Meta:
        model = Reservation
        fields = '__all__'

class EditCaseInfoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    room_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_in = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_out = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    
    
     
    class Meta:
        model = Reservation
        fields = '__all__'



class EditForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide customer\'s status -- '),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Rescheduled', 'Rescheduled'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    room_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_in = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_out = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))

    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS)

    class Meta:
        model = Reservation
        fields = '__all__'




class EditReservationInfoForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide customer\'s status -- '),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
        ('Rescheduled', 'Rescheduled'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    room_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_in = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    check_out = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS)
    
     
    class Meta:
        model = Reservation
        fields = '__all__'
