from django.contrib import admin
from .models import MyUser, ConfeRoom, Order

# Register your models here.
admin.site.register(MyUser)
admin.site.register(ConfeRoom)
admin.site.register(Order)