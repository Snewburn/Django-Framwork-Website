import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
import django
django.setup()

from AwardNominee.models import AwardNominee

for person in AwardNominee:
    person.delete();