from django.contrib import admin
from .models import Country,City,Bgroup,Booking
# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Bgroup)
admin.site.register(Booking)