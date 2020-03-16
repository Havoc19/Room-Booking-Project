from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
info = [
    {
        'name': 'OYO',
        'number': '345',
        'beds':'1',
        'date':'February 14,2020'
    },
    {
        'name': 'Nirmal HOTEL',
        'number': '346',
        'beds':'3',
        'date':'February 14,2020'
    }

]
def home(request):
    context = {
        'infos':info
    }
    return render(request, 'slot/home.html',context)

def about(request):
    return render(request, 'slot/about.html')