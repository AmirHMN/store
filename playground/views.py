from django.shortcuts import render
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay('hello')
    return render(request, 'hello.html', {'name': 'Amir'})
