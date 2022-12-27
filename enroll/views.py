from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.


def index(request):
    form = PlanForm
    if request.method == 'POST':
        form = PlanForm(request.POST)
        plan = request.POST['plan_type']
        if form.is_valid():
            # return redirect('/terms')
            if plan == str(1):
                return redirect('/terms')
            if plan == str(2):
                return redirect('/informal')

    context = {'form': form}
    return render(request, 'first.html', context)


def terms(request):
    form = CheckBox
    if request.method == 'POST':
        form = CheckBox(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/enrol_form')
    context = {'form': form}
    return render(request, 'terms.html', context)


def enrol(request):
    third = Enroll.objects.all()
    form = EnrolForm
    if request.method == 'POST':
        form = EnrolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    context = {'form': form, 'third': third}
    return render(request, 'enrol_form.html', context)


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capture')
    context = {'form': form}
    return render(request, 'register.html', context)


def load_stats(request):
    country_idm = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_idm)
    context = {'states': states}
    return render(request, 'state_dropdown_list_options.html', context)


def load_lga(request):
    state_main_id = request.GET.get('state_id')
    lgas = Lga.objects.filter(state_id=state_main_id)
    context = {'lgas': lgas}
    return render(request, 'lga_dropdown_list_options.html', context)


def load_town(request):
    lga_main_id = request.GET.get('lga_id')
    towns = Town.objects.filter(lga_id=lga_main_id)
    context = {'towns': towns}
    return render(request, 'town_dropdown_list_options.html', context)


def capture(request):
    method = Capture.objects.all()
    form = CaptureForm
    if request.method == 'POST':
        form = CaptureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful!')
            return redirect('/')
    context = {'form': form, 'method': method}
    return render(request, 'bio.html', context)


def informal(request):
    inform = Informal.objects.all()
    form = InFormalForm
    if request.method == 'POST':
        form = InFormalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    context = {'form': form, 'inform': inform}
    return render(request, 'informal.html', context)