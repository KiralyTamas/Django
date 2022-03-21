from django.shortcuts import render
from rewardapp.models import Passenger

def index(request):
    reward="Passenger Rewards"
    reward_dict={'reward':reward}
    return render(request, 'rewardapp/index.html',reward_dict)

def passenger(request):
    passenger=Passenger.objects.all()
    passenger_dict={'passenger':passenger}
    return render(request, 'rewardapp/passenger.html', passenger_dict)