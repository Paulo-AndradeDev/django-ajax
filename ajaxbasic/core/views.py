from django.shortcuts import render
from django.http import HttpResponse
from core.models import Profile
from django.db import IntegrityError


def create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        new_profile = Profile(full_name=full_name, bio=bio, email=email, phone=phone)

        try:
            new_profile.save()
            success = f'Profile Created Successfully for {full_name}'
            return HttpResponse(success)

        except IntegrityError:  # Específico para violações de integridade, como duplicatas em campos únicos
            return HttpResponse('There was an error saving the profile. Integrity violation.', status=400)

        except Exception as e:  # Captura qualquer outra exceção não especificamente tratada
            return HttpResponse(f'An error occurred: {e}', status=500)

    return HttpResponse("Invalid request", status=400)


def index(request):
    return render(request, 'index.html')

# def create(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         bio = request.POST.get('bio')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#
#         new_profile = Profile(full_name=full_name,bio=bio,email=email,phone=phone)
#         print(new_profile)
#         new_profile.save()
#         success = f'Profile Created Successfully for {full_name}'
#
#         return HttpResponse(success)