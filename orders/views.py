from django.shortcuts import render, redirect
from .models import Order
import pandas as pd
from django.contrib import messages
from .forms import UploadFileForm
from django.http import JsonResponse
from .models import CustomerOnboarding
from .forms import OnboardingForm
import logging 

def homepage(request):
    return render(request, 'homepage.html')
    
    

def order_status(request):
    order_id = request.GET.get('order_id')
    try:
        order = Order.objects.get(order_id=order_id)
        step = order.get_current_status() 
        expected_delivery = order.expected_delivery_date
        print(f"Found order: {order.customer_name}, Status: {order.status}")

        return render(request, 'orders/order_status.html', {
            'order': order,
            'step': step,
            'expected_delivery': expected_delivery,
            'status': order.status,
        })
    except Order.DoesNotExist:
        print(f"Order with ID {order_id} does not exist.")
        return render(request, 'orders/order_status.html', {
            'order_id': order_id,
        })


def upload_orders(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        data = pd.read_excel(excel_file)
        print(data.head()) 

        # Loop through each row in the Excel file
        for index, row in data.iterrows():
            order_id = row['order_id']
            customer_name = row['customer_name']
            status = row['status']
            expected_delivery_date = row['expected_delivery_date']

        
            order, created = Order.objects.update_or_create(
                order_id=order_id,  # Unique identifier
                defaults={
                    'customer_name': customer_name,
                    'status': status,
                    'expected_delivery_date': expected_delivery_date,
                }
            )

            if created:
                print(f"Order with ID {order_id} was created.")
            else:
                print(f"Order with ID {order_id} was updated.")

        return render(request, 'orders/upload.html', {'message': 'Orders updated successfully!'})

    return render(request, 'orders/upload.html')




import logging
logger = logging.getLogger(__name__)

def order_status_api(request,order_id):
    order_id = request.GET.get('order_id')
    
    order = Order.objects.get(id=order_id)
    logger.debug(f"Expected delivery date: {order.expected_delivery_date}")

    status_mapping = {
    'Order placed': 0,
    'Shipped': 1,
    'Out for Delivery': 2,
    'Delivered': 3
     }
    status_index = status_mapping.get(order.status, 3)
   
    return JsonResponse({'status': status_index})

logger = logging.getLogger(__name__)

def onboarding_form(request):
    if request.method == 'POST':
        # Handle the form submission here
        pass
    return render(request, 'orders/onboarding_form.html')

def confirmation_view(request):

    return render(request, 'orders/confirmation_page.html')

def submit_view(request):
    if request.method == 'POST':
        # Handle final form submission here
         return render(request, 'orders/success.html')
          
    return redirect('onboarding')



####################

def update_customer(request):
    return render(request, 'update_customer.html')

def ip_tools(request):
    return render(request, 'ip_tools.html')


def account(request):
    return render(request, 'account.html')
