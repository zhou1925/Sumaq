from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('meals/', include('meals.urls', namespace='meals')),
    path('api/', include('orders.api.urls', namespace='api')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]
