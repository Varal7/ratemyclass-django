from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rate.models import Student, Course, Assessment
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
            first_name=attributes['first_name'],
            last_name=attributes['last_name'],
            name=attributes['name'],
            promotion=attributes['promo'])

    return render(request, 'rate/home.html', {'student': student})


@login_required
def course(request, code):
    course = get_object_or_404(Course, code=code)
    assessments = Assessment.objects.filter(course = course)
    return render(request, 'rate/course.html', {'course': course, 'assessments': assessments})


@login_required
def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'rate/all_courses.html', {'courses': courses})
