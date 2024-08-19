from django.shortcuts import render
from django.utils import timezone


def homepage(request):
    return render(request, 'homepage.html', {
        'lab_name': 'Baranay',
        'current_time': timezone.now(),
    })
