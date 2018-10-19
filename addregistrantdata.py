import json
import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'Spencer_Assn10.settings'
django.setup()
from Registrant.models import Registrant

with open('registrant_data.json', 'r') as registrantData:
    dataObject = json.load(registrantData)

for registrant in dataObject['registrants']:
    entry = Registrant(
        Title=registrant['title'],
        FirstName=registrant['firstname'],
        LastName=registrant['lastname'],
        Address1=registrant['address1'],
        Address2=registrant['address2'],
        City=registrant['city'],
        State=registrant['state'],
        ZipCode=registrant['zipcode'],
        Telephone=registrant['telephone'],
        Email=registrant['email'],
        Website=registrant['email'],
        Position=registrant['position'],
        Company=registrant['company'],
        Meals=registrant['meals'],
        Billing_Firstname=registrant['billing_firstname'],
        Billing_Lastname=registrant['billing_lastname'],
        Card_Type=registrant['card_type'],
        Card_Number=registrant['card_number'],
        Card_CSV=registrant['card_csv'],
        Exp_Year=registrant['exp_year'],
        Exp_Month=registrant['exp_month'],
        Session1=registrant['session1'],
        Session2=registrant['session2'],
        Session3=registrant['session3']
    )
    entry.save()