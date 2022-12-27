from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Terms)
admin.site.register(Enroll)
admin.site.register(Registration)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Lga)
admin.site.register(Town)