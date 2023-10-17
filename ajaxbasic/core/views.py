from django.shortcuts import render
from django.http import HttpResponse
from core.models import Profile


def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        new_profile = Profile(full_name=full_name,bio=bio,email=email,phone=phone)
        print(new_profile)
        new_profile.save()
        success = f'Profile Created Successfully for {full_name}'

        return HttpResponse(success)