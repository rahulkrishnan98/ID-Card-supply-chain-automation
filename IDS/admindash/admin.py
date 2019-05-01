from django.contrib import admin
from .models import ClientDetail, OrderDetail, Uploadtemplate, GetData, Bill
# Register your models here.
admin.site.register(ClientDetail)
admin.site.register(OrderDetail)
admin.site.register(Uploadtemplate)
admin.site.register(GetData)
admin.site.register(Bill)
