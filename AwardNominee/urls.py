from django.conf.urls import url
from AwardNominee import views as award_views


urlpatterns = [
    url(r'^$', award_views.index, name="hello"),
    url(r'awards/', award_views.index, name="hello"),

]