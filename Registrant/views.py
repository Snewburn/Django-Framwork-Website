from Registrant.models import Registrant
from django.shortcuts import render
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
import django
django.setup()


def register(request):
    if request.method == 'POST':
        x = request.POST.get('FirstName')
        person = Registrant.objects.


    return render(request, 'registration.html')

