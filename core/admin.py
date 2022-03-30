from django.contrib import admin

# Register your models here.
from core.models import Region, Fruit

admin.site.register(Region)
admin.site.register(Fruit)
