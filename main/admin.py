from django.contrib import admin
from .models import ToDoList, Item,Daily
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Daily)

