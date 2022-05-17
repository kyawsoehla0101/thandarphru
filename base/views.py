from django.shortcuts import render

# Home View
def home(request):
    return render(request,'base/home.html')
    