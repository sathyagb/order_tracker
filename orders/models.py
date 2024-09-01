from django.db import models
from django.db.models import Model, CharField, DateField, IntegerField




class DocumentModel(models.Model):
    customer_name = models.CharField(max_length=255)
    iot_product_type = models.CharField(max_length=100)
    solution_document = models.FileField(upload_to='documents/')
    type2_file = models.FileField(upload_to='type2_files/')
    mdb_file = models.FileField(upload_to='mdb_files/')

class Order(Model):
    STATUS_CHOICES = [
        ('order_placed', 'Order placed'),
        ('shipped', 'Shipped'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    order_id = CharField(max_length=100, unique=True)
    customer_name = CharField(max_length=100)
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='order_placed')
    expected_delivery_date = DateField(null=True, blank=True)

    def get_current_status(self):
        if self.status == 'delivered':
            return 4
        elif self.status == 'out_for_delivery':
            return 3
        elif self.status == 'shipped':
            return 2
        else:
            return 1
        
class CustomerOnboarding(Model):
    customer_name = CharField(max_length=255)
    iot_product_type = CharField(max_length=255)
    apns_required =IntegerField()
    apn1 = CharField(max_length=255, blank=True, null=True)
    apn2 = CharField(max_length=255, blank=True, null=True)
    apn3 = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.customer_name





