from django.http import HttpResponse
from .models import Course
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def load_data(request):
    file = open('courses.json')

    courses = json.load(file)

    for course in courses:
        new_course = Course(title=course['title'], author=course['author'],
                            overview=course['overview'], image=course['img'],
                            url=course['url'])
        new_course.save()

    file.close()

    return HttpResponse('Data loaded successfully')


def list_data(request):
    course = Course.objects.all()
    return render(request, 'course.html', {'course': course})


def index(request):
    return HttpResponse("Hello")


@csrf_exempt
def deleteCourse(request, course_id):
    Item = Course.objects.get(id=course_id)
    Item.delete()
    return HttpResponseRedirect('/')


@csrf_exempt
def searchCourse(request):
    content = request.POST['query']
    items = Course.objects.filter(title__icontains=content)
    return render(request, 'course.html', {'course': items})
