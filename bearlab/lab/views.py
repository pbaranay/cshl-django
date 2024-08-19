from django.shortcuts import render

from .models import Staff


def staff_page(request, slug):
    try:
        staff = Staff.objects.get(slug=slug)
    except Staff.DoesNotExist:
        staff = None
    return render(request, 'staff_member.html',
    {'staff': staff})
