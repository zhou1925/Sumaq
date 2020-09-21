from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path(
        route='employee/', 
        view=views.dashboard_employee, 
        name='employee'),
    path('order/sent/<int:order_id>/',
        view=views.order_is_sent,
        name='order_is_sent'),
    path(
        route='owner/', 
        view=views.dashboard_owner, 
        name='owner'),
]