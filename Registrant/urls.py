from django.conf.urls import url
from Registrant import views as reg_views


urlpatterns = [
    url(r'^$', reg_views.register, name='regURL'),
]