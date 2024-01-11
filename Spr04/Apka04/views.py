from django.shortcuts import render

# Create your views here.

def spr04(request):
    context = {}
    return render(request, 'Apka04/spr04.html', context)