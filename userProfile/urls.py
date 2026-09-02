from django.utls import path
from . import views

app_name = 'userProfile'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.profile, name='profile_edit'),
]