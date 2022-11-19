from django.shortcuts import render
from signup.models import Signup,Vent

# Create your views here.
def index(request):
    return render(request, 'vent.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        id = Signup(username = username, password = password)
        id.save()

    return render(request, 'signup.html')

def vent(request):
    if request.method == "POST":
        problem = request.POST.get('problem')
        common = Vent(problem = problem)
        common.save()
    return render(request, 'vent.html')
def signin(request):
    return render(request, 'signin.html')

