from django.contrib import admin
from django.urls import path

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', MessagesAPIView.as_view(), name='messages'),
]
