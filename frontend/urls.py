from django.urls import path
from .views import home, about, contact, choose, tutorial, proceed

app_name = 'frontend'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('choose/operation/', choose, name='choose'),
    path('tutorial/', tutorial, name='tutorial'),
    path('exam/', proceed, name='proceed'),
]
