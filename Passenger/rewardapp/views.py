from django.shortcuts import render

def index(request):
    reward="Passenger Rewards"
    reward_dict={'reward':reward}
    return render(request, 'rewardapp/index.html',reward_dict)