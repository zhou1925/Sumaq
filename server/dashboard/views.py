from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order
from . import owner_data


def paginate(request, object_list):
    """ return pages employee dashboard """ 
    paginator = Paginator(object_list, 15)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return orders


@login_required
def dashboard_employee(request):
    """ List of orders to employee dashboard"""
    object_list = Order.objects.all().order_by('-created')
    orders = paginate(request=request, object_list=object_list)
    return render(request, 'dashboard/employee.html', {'orders': orders})


def order_is_sent(request, order_id):
    """ mark True if the order was sent """
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.sent = True
        order.save()
        return redirect('dashboard:employee')


@login_required
def dashboard_owner(request):
    """ return data for owner dashboard """
    meal_frecuency = owner_data.MealFrecuency()
    meal_frecuency.computeMealFrecuency()
    meal_labels = meal_frecuency.getMealLabels()
    meal_quantity =  meal_frecuency.getMealQuantity()

    totalSales = owner_data.total_sales()
    ordersPerMonth = owner_data.orders_per_month()
    salesOfEachMonth = owner_data.sales_per_month()
    orders = Order.objects.all()      
    return render(request, 'dashboard/owner.html',
                            {'orders': orders, 
                            'totalSales': totalSales,
                            'orders_per_month': ordersPerMonth,
                            'meal_labels': meal_labels,
                            'meal_quantity': meal_quantity,
                            'salesOfEachMonth': salesOfEachMonth})
