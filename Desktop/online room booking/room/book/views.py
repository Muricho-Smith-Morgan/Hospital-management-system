from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Reservation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .forms import EditForm, EditCaseInfoForm, EditReservationInfoForm
import datetime

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # login(request, user)
                return redirect("reception")
            else:
                messages.error(request, "invalid details")

    form = AuthenticationForm()

    return render(request, 'book/login.html', context={"login_form": form})

def book(request):
    # obj = Reservation.objects.get(id=pk)
    form = EditCaseInfoForm()
    if request.method == 'POST':
        form = EditCaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' details updated successfully.')
            return redirect('response')

    context = {'form': form}
    return render(request, 'book/book.html', context)


def index(request):
    return render(request, 'book/index.html',)

def reception(request):
    mydata = Reservation.objects.all().values()
    context = {'mymembers': mydata}
    return render(request, 'book/reception.html', context)

def response(request):
    return render(request, 'book/response.html',)

def update(request, pk):
    obj = Reservation.objects.get(id=pk)
    form = EditReservationInfoForm(instance=obj)
    if request.method == 'POST':
        form = EditReservationInfoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'details updated successfully.')
            return redirect('reception')

    context = {'form': form}
    return render(request, 'book/update.html', context)

            



    