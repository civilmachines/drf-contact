from django.conf.urls import url
from . import views


app_name = "drf_contact"


urlpatterns = [
    # ex: api/contacts/show/
    url(r'^show/', views.ShowContacts.as_view(), name='show-contact'),
    # ex: api/contacts/add/
    url(r'^add/', views.AddContacts.as_view(), name='add-contact'),
]
