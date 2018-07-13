from django.urls import path

from user.views import *

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/add', UserEntryForm.as_view()),
    path('users/delete', UserDelete.as_view()),
]
