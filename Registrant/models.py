from django.db import models


class Registrant(models.Model):
    theTitles = ((1, "Mr."), (2, "Mrs"), (3, "Ms"))
    theStates = (('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'),
                 ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
                 ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
                 ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'),
                 ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
                 ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'),
                 ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'),
                 ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
                 ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
                 ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
                 ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
                 ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'),
                 ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin)'),
                 ('WV', 'West Virginia'), ('WY', 'Wyoming'))
    theMeals = ((1, "MealPack"), (2, "Day 2 Dinner"), (3, "D2D"))
    theCards = ((1, "Visa"), (2, "Mastercard"), (3, "American Express"))
    session1names = ((1, "Structuring the Week"), (2, "Family based Youth ministry"), (3, "WHY"))
    session2names = ((1, "The heart of preaching"), (2, "Running a church summer camp"), (3, "HOW"))
    session3names = ((1, "Sermons that are effective"), (2, "Crises Intervention"),
                     (3, "Building a culture of evangelism"))
    Title = models.CharField(max_length=100, choices=theTitles)
    FirstName = models.CharField(max_length=200, default="empty")
    LastName = models.CharField(max_length=200, default="empty")
    Address1 = models.CharField(max_length=200, default="empty")
    Address2 = models.CharField(max_length=200, default="empty")
    City = models.CharField(max_length=200, default="empty")
    State = models.CharField(max_length=100, choices=theStates)
    ZipCode = models.IntegerField()
    Telephone = models.CharField(max_length=100, default="empty")
    Email = models.EmailField()
    Website = models.URLField()
    Position = models.CharField(max_length=200, default="empty")
    Company = models.CharField(max_length=200, default="empty")
    Meals = models.CharField(max_length=100, choices=theMeals)
    Billing_Firstname = models.CharField(max_length=200, default="empty")
    Billing_Lastname = models.CharField(max_length=200, default="empty")
    Card_Type = models.CharField(max_length=100, choices=theCards)
    Card_Number = models.IntegerField()
    Card_CSV = models.IntegerField()
    Exp_Year = models.IntegerField()
    Exp_Month = models.IntegerField()
    Session1 = models.CharField(max_length=100, choices=session1names)
    Session2 = models.CharField(max_length=100, choices=session2names)
    Session3 = models.CharField(max_length=100, choices=session3names)