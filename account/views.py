from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def main_view(request):
    return render(request, 'main.html')

def passport_view(request):
    return render(request, 'passport.html')

def save_passport_mo(request):
    if request.method == 'POST':
        return HttpResponse("Data saved successfully")
    return redirect('passport')

def reference_info(request):
    return render(request, 'reference_info.html')