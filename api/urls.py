from django.urls import path, include

from .views import *


app_name = 'api'

urlpatterns = [
    path('clients/', include('api.clients.urls')),
    path('list/', UsersListView.as_view()),
]