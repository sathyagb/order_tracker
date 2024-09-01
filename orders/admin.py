from django.contrib import admin
from .models import Order 
from .models import CustomerOnboarding

admin.site.register(Order)
admin.site.register(CustomerOnboarding)