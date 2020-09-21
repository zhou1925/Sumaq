from orders.models import Order


def total_sales():
    """ return total sales of orders """
    data = []
    orders = Order.objects.all()
    for order in orders:
        data.append(order.get_total_cost())
    return sum(data)


def orders_per_month():
    """ return quantity of orders per each month """
    months = []
    month = 1
    for _ in range(12):
        months.append(Order.objects.filter(created__month=f'{month}').count())
        month += 1
    return months


# O(n^2)
def sales_per_month():
    salesOfEachMonth = []
    currentMonthOrders = []
    currentMonthSales = []
    month = 1
    for _ in range(12):
        currentMonthOrders = Order.objects.filter(created__month=f'{month}')
        for order in currentMonthOrders:
            currentMonthSales.append(int(order.get_total_cost()))
        salesOfEachMonth.append(sum(currentMonthSales))
        month += 1
    return salesOfEachMonth

# 1. get, return data of order objects
# 2. get values of an order object
# 3. compute frecuency of an str in an meals list
# 4. return frequency and quantity
class MealFrecuency:
    def __init__(self):
        self.data = {}
        self.labels = []
        self.quantity = []
        self.meals = []
    
    # O(n^2)
    def getOrdersData(self):
        """ get order objects and fill data: order_id: name_order_object """
        orders = Order.objects.all()
        id_order = 1
        for order in orders:
            for item in order.items.all():
                self.data[f'{id_order}'] = {'name': item.meal.name}
                id_order += 1

    # O(n^2)
    def getOrderValues(self):
        """ fill meals with values of each order """
        for order_item in self.data.values():
            for value in order_item.values():
                if type(value) == str:
                    self.meals.append(value)
    
    def computeMealFrecuency(self):
        """ compute frecuency of meal name and his quantity """
        self.getOrdersData()
        self.getOrderValues()
        meals = set(self.meals)
        for meal in meals:
            self.labels.append(meal)
            self.quantity.append(self.meals.count(meal))
    
    def getMealLabels(self):
        """ return meal label """ 
        return self.labels
    
    def getMealQuantity(self):
        """ return meal quantity """
        return self.quantity
