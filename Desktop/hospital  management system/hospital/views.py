from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from .models import Patient
from django.contrib import messages
from django.template import loader
from .forms import EditForm, EditPatientInfoForm


# Create your views here.

def hello(request):
    return render(request, 'hospital/hello.html',)

def appointment(request):
    return render(request, 'hospital/appointment.html')

def About(request):
    return render(request, 'hospital/About.html',)

def Contact(request):
    return render(request, 'hospital/Contact.html',)



def Doctor(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password1 = request.POST['Password1']
        user = auth.authenticate(username = Username, password = Password1)

        if user is not None:
            auth.login(request, user)
            return redirect('Doctor_panel')
        else:
            messages.error(request, 'Invalid details')
            return redirect('Doctor')
    else:
        return render(request, 'hospital/Doctor.html')
        
    return render(request, 'hospital/Doctor.html')

def Receptionist(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Password1 = request.POST['Password1']
        user = auth.authenticate(username = Username, password = Password1)

        if user is not None:
            auth.login(request, user)
            return redirect('reception')
        else:
            messages.error(request, 'Invalid details')
            return redirect('Receptionist')
    
    return render(request, 'hospital/Receptionist.html')



def reception(request):
    return render(request, 'hospital/Reception_panel.html')

def Doctor_panel(request):
    all_patients = Patient.objects.all()

    context = {'patients': all_patients}
    return render(request, 'hospital/Doctor_panel.html', context)

def Reception_panel(request):
    return render(request, 'hospital/Reception_panel.html')    

def Add_patient(request):
    if request.method == 'POST':
        f_name = request.POST['firstname']
        phone_no = request.POST['phonenumber']
        email = request.POST['email']
        residence = request.POST['Residence']
        national_id = request.POST['national_id']

        patient_info = Patient.objects.create(first_name=f_name, phone_number=phone_no, email=email, residence=residence, national_id=national_id)
        patient_info.save()

        return redirect('View_patient')
    
    
    return render(request, 'hospital/Add_patient.html')

def View_patient(request):
    mydata = Patient.objects.all().values()
    context = {'mymembers': mydata}
    return render(request, 'hospital/View_patient.html', context)

def Emergency(request):
    return render(request, 'hospital/Emergency.html')

def edit_patient_info(request, pk):
    patient = Patient.objects.get(id=pk)
    form = EditForm(instance=patient)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('View_patient')
        

    context = {'edit_form': form}
    return render(request, 'hospital/edit.html', context)

def delete_patient_info(request, pk):
    obj = Patient.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, 'Patient details deleted successfully.')
        return redirect('View_patient')

    context = {'obj': obj}
    return render(request, 'hospital/delete.html', context)


def edit_patient_status(request, pk):
    obj = Patient.objects.get(id=pk)
    form = EditPatientInfoForm(instance=obj)
    if request.method == 'POST':
        form = EditPatientInfoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient details updated successfully.')
            return redirect('Doctor_panel')

    context = {'form': form}
    return render(request, 'hospital/doctor_edit.html', context)