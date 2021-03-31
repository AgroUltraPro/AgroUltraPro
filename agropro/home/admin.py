from django.contrib import admin
from .models import Farmer,Wholesaler,Notification,Crop
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Wholesaler)
admin.site.register(Notification)
admin.site.register(Crop)

'''
from django.apps import apps
from django.contrib import admin

models = apps.get_models()

for model in models:
    admin.site.register(model)'''