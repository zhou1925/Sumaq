from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path(
        route='orders/',
        view=views.OrderListView.as_view(),
        name='order_list'
    ),
    path(
        route='orders/<pk>/',
        view=views.OrderDetailView.as_view(),
        name='order_detail'
    )
]
