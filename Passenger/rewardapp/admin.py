from django.contrib import admin
from rewardapp.models import Passenger

class PassengerAdmin(admin.ModelAdmin):
    list_display=('firstName','lastName','email','reward_point')
    
admin.site.register(Passenger,PassengerAdmin)