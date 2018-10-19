import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
import django
django.setup()

from conferencesite.models import Workshop

thing1 = Workshop(
    Name="Structuring the Week",
    Session="Session 1",
    Room_Number="Room1",
    Start_Time="1:00 pm",
    End_Time="3:30 pm"
)

thing2 = Workshop(
    Name="Family Based youth Ministry",
    Session="Session 1",
    Room_Number="Room 2",
    Start_Time="1:00 pm",
    End_Time="3:00 pm"
)

thing3 = Workshop(
    Name="Why?",
    Session="Session 1",
    Room_Number="Room 3",
    Start_Time="1:00 pm",
    End_Time="3:00pm"
)

thing4 = Workshop(
    Name="The heart of preaching",
    Session="Session 2",
    Room_Number="Room 1",
    Start_Time="9:00 am",
    End_Time="12:00pm"
)

thing5 = Workshop(
    Name="Running a church summer camp",
    Session="Session 2",
    Room_Number="Room 2",
    Start_Time="9:00 am",
    End_Time="12:00 pm"
)

thing6 = Workshop(
    Name="How?",
    Session="Session 2",
    Room_Number="Room 3",
    Start_Time="9:00 am",
    End_Time="12:00 pm"
)

thing7 = Workshop(
    Name="Sermons that are effective",
    Session="Session 3",
    Room_Number="Room 1",
    Start_Time="1:00 pm",
    End_Time="3:00 pm"
)

thing8 = Workshop(
    Name="Crises intervention",
    Session="Session 3",
    Room_Number="Room 2",
    Start_Time="1:00 pm",
    End_Time="3:00 pm"
)

thing9 = Workshop(
    Name="Building a culture of evangelism",
    Session="Session 3",
    Room_Number="Room 3",
    Start_Time="1:00 pm",
    End_Time="3:00 pm"
)

thing1.save()
thing2.save()
thing3.save()
thing4.save()
thing5.save()
thing6.save()
thing7.save()
thing8.save()
thing9.save()