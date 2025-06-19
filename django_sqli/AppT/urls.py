from django.urls import path
from .views import vul_view
urlpatterns = [
    path('vul/', vul_view, name='vul_view'),
]