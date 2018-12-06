from django.urls import path
from .views import ListContactsView


urlpatterns = [
    path('contacts/', ListContactsView.as_view(), name="contacts-all")
]