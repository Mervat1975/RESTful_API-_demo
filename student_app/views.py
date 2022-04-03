
from django.shortcuts import render

from student_app.models import Student


def index(request):
    context = {
        'students': Student.objects.all(),
    }
    # return render(request, 'student_app/student_list.html', context)
    return render(request, 'index.html', context)


def show(request, id):
    context = {
        'student': Student.objects.get(id=id),
        'students': Student.objects.all(),
    }
    # eturn render(request, 'student_app/student.html', context)
    return render(request, 'index.html', context)
