from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('staff/', views.staff_list, name='staff_list'),
    path('logout/', views.logout_view, name='logout')

]
