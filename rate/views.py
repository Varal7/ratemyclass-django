from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rate.models import Student, Course, Assessment
import json


def home(request):
    student = Student.objects.get(user = request.user)
    return render(request, 'rate/home.html', {'student': student})


def course(request, code):
    course = get_object_or_404(Course, code=code)
    assessments = Assessment.objects.filter(course = course)
    return render(request, 'rate/course.html', {'course': course, 'assessments': assessments})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'rate/all_courses.html', {'courses': courses})
