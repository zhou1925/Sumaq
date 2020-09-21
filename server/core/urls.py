from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path(
        route='',
        view=views.home,
        name='home'),
    path(
        route='about/',
        view=views.about,
        name='about'),
]
