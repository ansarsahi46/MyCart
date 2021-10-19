from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Contact
from .models import orders
from .models import orderUpdate

admin.site.register(orders)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(orderUpdate)