# persondetails_app/urls.py
from django.urls import path
from .views import person_details
from .views import create_person
from .views import calculate_interest, interest_result, login_view
urlpatterns = [
    path('', person_details, name='home'),
path('create/', create_person, name='create_person'),
path('calculate/', calculate_interest, name='calculate_interest'),
    path('result/<int:pk>/', interest_result, name='interest_result'),
    path('login/', login_view, name='login'),

]

