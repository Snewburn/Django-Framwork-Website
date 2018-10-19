

from AwardNominee.models import AwardNominee
from django.shortcuts import render

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
import django
django.setup()


def index(request):
    if request.method == 'POST':
        x = request.POST.get('vote')
        choice = AwardNominee.objects.get(Name=x)
        y = int(choice.Num_Votes)
        y = y + 1
        z = str(y)
        choice.Num_Votes = z
        choice.save()
    nominee_list = AwardNominee.objects.all()
    context = {'AwardNominee': nominee_list}
    return render(request, 'awards.html', context)



