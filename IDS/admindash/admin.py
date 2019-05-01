from django.contrib import admin
from .models import ClientDetail, OrderDetail, Uploadtemplate, GetData
# Register your models here.
admin.site.register(ClientDetail)
admin.site.register(OrderDetail)
admin.site.register(Uploadtemplate)
admin.site.register(GetData)
