# Create your views here.
from django.shortcuts import render
from .models import Sign
import random

def index(request):
    count = Sign.objects.count()
    random_index = random.randint(0, count - 1)
    sign = Sign.objects.all()[random_index]
    return render(request, 'todaysignlan/index.html', {'sign': sign})