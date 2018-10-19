import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
import django
django.setup()

from AwardNominee.models import AwardNominee


person = AwardNominee(
    Name="Mitch David",
    Description="Bible is Barley used",
    Image_name="Empty",
    Num_Votes="2"
)

person2 = AwardNominee(
    Name="Mike Murphy",
    Description="Bible is Worn",
    Image_name="preacher2.jpg",
    Num_Votes="10"
)

person3 = AwardNominee(
    Name="Steven Jacobs",
    Description="Bible is Memorized",
    Image_name="Empty",
    Num_Votes="4"
)

person.save()
person2.save()
person3.save()