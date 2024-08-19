from django.urls import path
from .views import order_status, upload_orders
from . import views 


urlpatterns = [
    path("homepage/", views.homepage, name="homepage"), #homepage
    path("status/", views.order_status, name="order_status"), #status
    path('upload/', views.upload_orders, name='upload_orders'),
    path('order_status_api/', views.order_status_api, name='order_status_api'),
    path('onboarding/', views.onboarding_form, name='onboarding_form'), #customer onboarding
    path('confirmation/', views.confirmation_view, name='confirmation'),
    path('submit/', views.submit_view, name='submit'),
    #path('success/', views.success_page, name='success_page'),

    path('update_customer/', views.update_customer, name='update_customer'),
    path('ip_tools/', views.ip_tools, name='ip_tools'),
    path('account/', views.account, name='account'),
    
]
