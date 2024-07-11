from django.shortcuts import render
from django.http import HttpResponse
from .models import Services

# Create your views here.
def index(request):
    service1 = Services()
    service1.id = 0
    service1.name = 'Fast'
    service1.description = 'Our Services is very fast'

    service2 = Services()
    service2.id = 1
    service2.name = 'Reliable'
    service2.description = 'Our Services is very Reliable'

    service3 = Services()
    service3.id = 2
    service3.name = 'Affordable'
    service3.description = 'Our Services is very Cheap'

    service4 = Services()
    service4.id = 3
    service4.name = 'Easy to Use'
    service4.description = 'Our Services is Easy to Use'

    service = [service1, service2, service3, service4]
    return render(request, 'index.html', {'services': service})