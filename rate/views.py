from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rate.models import Student
import json


@login_required
def home(request):
    attributes = request.session['attributes']
    try:
        student = Student.objects.get(user__username=request.user.username)
    except Student.DoesNotExist:
        # For the first connection, we create a student
        user = User.objects.get(username=request.user.username)
        student = Student.objects.create(user=user,
            name=attributes['name'],
            promotion=attributes['promo'])

    return render(request, 'home.html', {'student': student})
