from django.utils import timezone
from django.shortcuts import render


def homepage(request):
    # context
    return render(request, 'homepage.html', {
        'lab_name': 'Baranay',
        'current_time': timezone.now(),
    })
