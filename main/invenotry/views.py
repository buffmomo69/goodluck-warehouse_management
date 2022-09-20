# from multiprocessing import context
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .filters import MarkaFilter
from .forms import *


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'templates/login.html', context)


@login_required(login_url='login')
def home(request):
    markas = Marka.objects.all()
    
    
    # search functionality
    markafilter = MarkaFilter(request.GET, queryset=markas)
    markas = markafilter.qs

    context = {
        'markas': markas,
        'markafilter': markafilter,
    }
    return render(request, 'index.html', context)


# @login_required(login_url='login')


@login_required(login_url='login')
def add_container(request):
    forms = ContainerEntryForm(request.POST)
    if request.method == "POST":
        if forms.is_valid():
            try:
                forms.save()
                return redirect('add_stock')
            except IntegrityError as error:
                if 'UNIQUE constraint' in str(error.args):
                    errormessage = "The Given Container Number Already Exists Enter a New Container Number"
                    return render(request, 'add_container.html', {"forms": forms, "errormessage": errormessage})
                else:
                    errormessage = "Some Error Occoured"
                    return render(request, 'add_container.html', {"forms": forms, "errormessage": errormessage})

        else:
            forms = ContainerEntryForm()
            return render(request, 'add_container.html', {"forms": forms})

    return render(request, 'add_container.html', {"forms": forms})


# @login_required(login_url='login')
def add_firm(request):
    forms = FirmEntryForm(request.POST)
    if request.method == "POST":
        if forms.is_valid():
            try:
                forms.save()
                return redirect('add_firm')
            except IntegrityError as error:
                print(error)
                if 'UNIQUE constraint' in str(error.args):
                    errormessage = "The Given Container Number Already Exists Enter a New Container Number"
                    return render(request, 'add_firm.html', {"forms": forms, "errormessage": errormessage})
                else:
                    print(error.args)
                    errormessage = "Some Error Occoured"
                    print(errormessage)

                    return render(request, 'add_firm.html', {"forms": forms, "errormessage": errormessage})

        else:
            forms = ContainerEntryForm()

            print(forms.errors)
            return render(request, 'add_firm.html', {"forms": forms})

    print(forms.errors)
    return render(request, 'add_firm.html', {"forms": forms})


def add_stock(request):
    forms = StockEntryForm(request.POST)
    if request.method == "POST":
        print(str(forms.is_valid()) + " " + "Add Stock Called")
        if forms.is_valid():
            forms.save()
            return redirect('add_stock')
        else:
            forms = ContainerEntryForm()
    return render(request, 'add_stock.html', {"forms": forms})



# class update_stock
def update_stock(request,pk):
    
    marka=Marka.objects.get(id=pk)
    forms = StockEntryForm(instance=marka)
    print(marka)
    print(str(forms.is_valid()) + " " + "Update Stock Called")
    
    if request.method == "POST":
        forms=StockEntryForm(request.POST,instance=marka)
        
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    context={'forms':forms,'marka':marka}
    return render(request, 'update_stock.html', {"forms": forms,"marka":marka})
    